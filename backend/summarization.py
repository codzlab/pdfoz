# backend/summarization.py

# You can implement text summarization algorithms here
# backend/summarization.py
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from heapq import nlargest

def generate_summary(text, num_sentences=3):
    """
    Generate a summary of the input text.

    Args:
        text (str): Input text to be summarized.
        num_sentences (int): Number of sentences to include in the summary. Default is 3.

    Returns:
        str: Summary of the input text.
    """
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Tokenize each sentence into words
    words = [word.lower() for sentence in sentences for word in word_tokenize(sentence)]

    # Filter out stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Calculate word frequency
    word_freq = FreqDist(words)

    # Assign a score to each sentence based on the sum of the frequencies of its words
    sentence_scores = {sentence: sum(word_freq[word] for word in word_tokenize(sentence)) for sentence in sentences}

    # Select the top N sentences with the highest scores
    summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

    # Join the selected sentences to form the summary
    summary = ' '.join(summary_sentences)

    return summary

# For example, using NLTK, Gensim, or other libraries
