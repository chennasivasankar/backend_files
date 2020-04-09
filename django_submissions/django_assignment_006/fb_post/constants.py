from enum import Enum


class ReactionEnum(Enum):
    WOW='WOW'
    LIT='LIT'
    LOVE='LOVE'
    HAHA="HAHA"
    THUMBS_UP='THUMBS-UP'
    THUMBS_DOWN='THUMBS-DOWN'
    ANGRY='ANGRY'
    SAD='SAD'
    
    
    @classmethod
    def reactions(cls):
        return [reaction.value for reaction in ReactionEnum]
    
    @classmethod
    def positive_reactions(cls):
        return [
            'THUMBS-UP',
            'LIT',
            'HAHA',
            'LOVE',
            'WOW'
            ]
    
    @classmethod
    def negative_reactions(cls):
        return [
            'SAD',
            'ANGRY',
            'THUMBS-DOWN'
            ]

class PostiveReactionEnum(Enum):
    THUMBS_UP='THUMBS-UP'
    LIT='LIT'
    HAHA='HAHA'
    LOVE='LOVE'
    WOW='WOW'

class NegativeReactionEnum(Enum):
    SAD='SAD'
    ANGRY='ANGRY'
    THUMBS_DOWN='THUMBS-DOWN'