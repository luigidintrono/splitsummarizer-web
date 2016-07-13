from flask_wtf import Form
from wtforms import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.lex_rank import LexRankSummarizer 

class SourceTextGrabber(Form):
    source_text = StringField(u'Text',
                            validators=[DataRequired()],
                            widget=TextArea())


def get_summary(source_text, compression_factor):
    """
    Given some input source_text, returns its summary based on the chosen 
    compression factor.
    """
    summary = {
        'source_text': source_text,
        'compression_factor': compression_factor,
        'summary': '',
        'success': False
    }
    
    parser = PlaintextParser.from_string(source_text, Tokenizer("english"))
    summ_algo = LexRankSummarizer()
    final_line_num = \
        int(source_text.count('.')/compression_factor)
    try:
        raw_summary = summ_algo(parser.document, final_line_num)
        for sentence in raw_summary:
            summary['summary'] += str(sentence) + ' '
    except:
        pass

    summary['success'] = (len(summary['summary']) != 0)

    return summary
