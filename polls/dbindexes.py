from .models import Choice
from dbindexer.api import register_index

register_index(Choice, {
    'poll__pub_date': 'year',
})
