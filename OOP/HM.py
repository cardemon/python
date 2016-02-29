class Lonely:
    """class with one Instance
       task #1
    """
    lone_instance = None

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    male1 = ("Robert",22,"male")
    female1 = ("Ann",87,"female")

class Observable:
    """task #2"""
    def __init__(self, name, work, jobs, titles):
        self.name = name
        self.work = work
        self.jobs = jobs
        self.titles = titles

    def __repr__(self):
        return 'Observable(name:{}, work:{}, jobs:{}, titles:{})'

first = Observable(name='Henry', work='baker', jobs=('baker',"2 month"), titles=('certified baker'))

class RegexValidator():
    """task #3"""
    def __init__(self, regex, message):
        self.regex = regex
        self.message = message

    def __call__(self, text):
        self.text = text
        if (self.regex != self.text):
            print self.message
        else:
            print str (self.text) + "nice"

valid1 = RegexValidator(regex='^[A-Z]', message="nope")
valid2 = ('check1')
valid3 = ('dqdqwd')
valid4 = ('F')


class EmailValidatior(RegexValidator):
    """task #3 (b)"""
    def __init__(self):
        RegexValidator.__init__(self, regex='[\w.]+[@][\w.][a-z]', message='Check ur address!')

email_valid = EmailValidatior()
email_valid('ruslan228.com')
email_valid('ruslanpitula@yahoo.com')
email_valid('wtf.com.ua')
email_valid('ruslan.555@ukr.net')
