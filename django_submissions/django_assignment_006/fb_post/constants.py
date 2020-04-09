from enum import Enum


class ReactionEnum(Enum):
    WOW=1
    LIT=2
    LOVE=3
    HAHA=4
    THUMBS_UP=5
    THUMBS_DOWN=6
    ANGRY=7
    SAD=8
    
    
    @classmethod
    def reactions(cls):
        return [
            'WOW',
            'LIT',
            'LOVE',
            'HAHA',
            'THUMBS-DOWN',
            'THUMBS-UP',
            'ANGRY',
            'SAD'
            ]
    
    @classmethod
    def positive_reactions(cls):
        return [
            'THUMBS-UP',
            'LIT',
            'LOVE',
            'HAHA',
            'WOW'
            ]
    
    @classmethod
    def negative_reactions(cls):
        return [
            'SAD',
            'ANGRY',
            'THUMBS-DOWN'
            ]