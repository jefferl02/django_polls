from sileo.sileo.resource import Resource
from sileo.sileo.fields import ResourceTypeConvert, ResourceModelManager
from polls.models import Question
from polls.forms import QuestionForm
from sileo.sileo.registration import register

class QuestionResource(Resource):
    query_set = Question.objects.all()
    allowed_methods = ['filter']
    fields = [
        'pk', 'question_text',
        ResourceTypeConvert('pub_date', str)
        # ResourceModelManager('choices', resource=ChoiceResource)
    ]

register('polls', 'questions', QuestionResource, version='v1')