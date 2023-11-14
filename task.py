
class Story:

    def __init__(self):
        self.main_story = '' 

    def add_sentence(self, text):
        self.main_story = self.main_story + ' ' + text


    def display_story(self):
        return self.main_story


if __name__ == '__main__':

    story = Story()

    story.add_sentence('i went to school')

    print(story.display_story())

    story.add_sentence('it rained that day.')
    story.add_sentence('i got very wet.')

    print(story.display_story()) 