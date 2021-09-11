# -*- coding: utf-8 -*-
"""
@author: eltsovt
"""
# Function to make word cloud
import matplotlib.pyplot as plt
# from word_cloud import WordCloud
from wordcloud import WordCloud


# To create a wordcloud one needs to have a file with frequencies and words named
# all_sigrams.tsv in the same dirrectory as the word_cl.py file.

handle = open('all_sigrams.tsv', 'r')
d = {}
for line in handle:
    words = line.split('\t')
    # words[1].rstrip('\n')
    d[words[0]] = int(words[1])

wordcloud = WordCloud(width=1100, height=900, background_color='white')
wordcloud.generate_from_frequencies(frequencies=d)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.tight_layout()
plt.axis("off")
plt.savefig('picture.png', dpi=400, bbox_inches='tight')
plt.show()

#clear plot
plt.clf()
plt.close('all')

