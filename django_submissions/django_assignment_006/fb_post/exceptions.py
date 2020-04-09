class Error(Exception):
    pass

class InvalidUserException(Error):
    pass

class InvalidPostContent(Error):
    pass

class InvalidPostException(Error):
    pass

class InvalidCommentContent(Error):
    pass

class InvalidCommentException(Error):
    pass

class InvalidReplyContent(Error):
    pass

class InvalidReactionTypeException(Error):
    pass

class UserCannotDeletePostException(Error):
    pass