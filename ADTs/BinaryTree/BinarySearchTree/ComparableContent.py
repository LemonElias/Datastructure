class ComparableContent:
    # Create class: ComparableContent
    def __init__(self, pContent):
        self.content = pContent

    def isGreater(self, pContent):
        return self.content > pContent # Checks if the content is greater than the given content

    def isLess(self, pContent):
        return self.content < pContent # Checks if the content is less than the given content
    
    def isEqual(self, pContent):
        return self.content == pContent # Checks if the content is equal to the given content