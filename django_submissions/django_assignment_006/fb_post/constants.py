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
    def choices(cls):
        return [reaction.value for reaction in ReactionEnum]
    
    @classmethod
    def choices_tuple(cls):
        return [(reaction.key,reaction.value) for reaction in ReactionEnum]
    

class PositiveReactionEnum(Enum):
    THUMBS_UP='THUMBS-UP'
    LIT='LIT'
    HAHA='HAHA'
    LOVE='LOVE'
    WOW='WOW'
    
    @classmethod
    def choices(cls):
        return [reaction.value for reaction in PositiveReactionEnum]


class NegativeReactionEnum(Enum):
    SAD='SAD'
    ANGRY='ANGRY'
    THUMBS_DOWN='THUMBS-DOWN'
    
    @classmethod
    def choices(cls):
        return [reaction.value for reaction in NegativeReactionEnum]