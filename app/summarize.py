"""
Main script that does summarizing for us.
"""
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.lex_rank import LexRankSummarizer 



def get_summary(text):
    """
    Given some input text, returns its summary.
    """
    summarized = ''
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()

    num_lines = text.count('.')
    summary = summarizer(parser.document, round(num_lines/3))

    for sentence in summary:
        summarized += str(sentence) + ' '

    return summarized   
