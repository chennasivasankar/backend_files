from .models import *
import datetime
from .exceptions import *
from django.db.models import *
from django.db import *
from .constants import *


#Verification Functions

def check_valid_user_id(user_id):
    if(not(User.objects.filter(id=user_id).exists())):
        raise InvalidUserException

def check_valid_post_id(post_id):
    if(not(Post.objects.filter(id=post_id).exists())):
        raise InvalidPostException

def check_valid_comment_id(comment_id):
    if(not(Comment.objects.filter(id=comment_id).exists())):
        raise InvalidCommentException


def check_for_non_empty_post_content(post_content):
    if(post_content==''):
        raise InvalidPostContent
    
def check_for_non_empty_comment_content(comment_content):
    if(comment_content==''):
        raise InvalidCommentContent

def check_for_non_empty_reply_content(reply_content):
    if(reply_content==''):
        raise InvalidReplyContent


#Assignment-6


#Task-2

def create_post(user_id,post_content=''):
    #Verification
    check_valid_user_id(user_id)
    check_for_non_empty_post_content(post_content)
    
    #Functionality
    post= Post.objects.create(
            posted_by_id=user_id,
            posted_at=datetime.datetime.now(),
            content=post_content
            )
    return post.id

#Task-3

def create_comment(user_id,post_id,comment_content=''):
    #Verification
    check_valid_user_id(user_id)
    check_valid_post_id(post_id)
    check_for_non_empty_comment_content(comment_content)
    
    #Functionality
    comment=Comment.objects.create(
                        content=comment_content,
                        commented_at=datetime.datetime.now(),
                        commented_by_id=user_id,
                        post_id=post_id,
                    )

    return comment.id


#Task-4

def reply_to_comment(user_id, comment_id, reply_content=''):
    #Verification
    check_valid_user_id(user_id)
    check_for_non_empty_reply_content(reply_content)
    
    #Functionality
    try:
        comment_obj=Comment.objects.get(id=comment_id)
        if(comment_obj.parent_comment_id):
            parent_id=comment_obj.parent_comment_id
        else:
            parent_id=comment_id
        reply = Comment.objects.create(
                content=reply_content,
                commented_at=datetime.datetime.now(),
                commented_by_id=user_id,
                post_id=comment_obj.post_id,
                parent_comment_id=parent_id
            )
    except Comment.DoesNotExist:
        raise InvalidCommentException
        
    return reply.id




#Task-5-Enum

def react_to_post(user_id, post_id, reaction_type):
    #Verification
    check_valid_user_id(user_id)
    check_valid_post_id(post_id)
    
    #Functionality
    prev_reaction=Reaction.objects.filter(
                        reacted_by_id=user_id,
                        post_id=post_id
                    )
    try:
        ReactionEnum(reaction_type)
    except ValueError:
        raise InvalidReactionTypeException
    else:
        if prev_reaction and prev_reaction[0].reaction==reaction_type:
            prev_reaction[0].delete()
        elif prev_reaction and prev_reaction[0].reaction!=reaction_type:
            prev_reaction[0].reaction=reaction_type
            prev_reaction[0].reacted_at=datetime.datetime.now()
            prev_reaction[0].save()
        else:    
            Reaction.objects.create(
                post_id=post_id,
                reaction=reaction_type,
                reacted_at=datetime.datetime.now(),
                reacted_by_id=user_id
                )                
        

#Task-6-Enum

def react_to_comment(user_id, comment_id, reaction_type):
    #Verification
    check_valid_user_id(user_id)
    check_valid_comment_id(comment_id)
    
    #Functionality
    
    prev_reaction=Reaction.objects.filter(
                        reacted_by_id=user_id,
                        comment_id=comment_id
                    )
    try:
        ReactionEnum(reaction_type)
    except:
        raise InvalidReactionTypeException
    else:
        if prev_reaction and prev_reaction[0].reaction==reaction_type:
            prev_reaction[0].delete()
        elif prev_reaction and prev_reaction[0].reaction!=reaction_type:
            prev_reaction[0].reaction=reaction_type
            prev_reaction[0].reacted_at=datetime.datetime.now()
            prev_reaction[0].save()
        else:    
            Reaction.objects.create(
                comment_id=comment_id,
                reaction=reaction_type,
                reacted_at=datetime.datetime.now(),
                reacted_by_id=user_id
                )
    

#Task-7

def get_total_reaction_count():
    return Reaction.objects.aggregate(count=Count('id'))


#Task-8

def get_reaction_metrics(post_id):
    #Verification
    check_valid_post_id(post_id)
    
    #Functionality
    reaction_metrics=Reaction.objects.filter(
                post_id=2
            ).values_list(
                'reaction'
            ).annotate(
                Count('id')
                ).order_by('-id__count')

    return dict(reaction_metrics)


#Task-9

def delete_post(user_id, post_id):
    #Verification
    check_valid_user_id(user_id)
    
    #Functionality
    try:
        post=Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise InvalidPostException
    else:
        if(post.posted_by_id==user_id):
            post.delete()
        else:
            raise UserCannotDeletePostException
    

#Task-10

def get_posts_with_more_positive_reactions():
    reaction_metrics=Reaction.objects.filter(
            post_id__isnull=False
        ).values('post_id').annotate(
            positive_reactions=Count('reaction',
                filter=Q(reaction__in=PositiveReactionEnum.choices())
            ),
            negative_reactions=Count('reaction',
                filter=Q(reaction__in=NegativeReactionEnum.choices())
            )
        ).filter(
            positive_reactions__gt=F('negative_reactions')
        ).values_list('post_id',flat=True)
    return list(reaction_metrics)


#Task-11

def get_posts_reacted_by_user(user_id):
    #Verification
    check_valid_user_id(user_id)
    
    #Functionality
    reacted_posts=Reaction.objects.filter(
            reacted_by_id=user_id,
            post_id__isnull=False
            ).values_list(
                'post_id',flat=True
            ).distinct()
            
    return list(reacted_posts)


#Task-12

def get_reactions_to_post(post_id):
    #Verification
    check_valid_post_id(post_id)
    
    #Functionality
    post_reactions_details=[]
    post_reactions=Reaction.objects.filter(
        post_id=post_id
        ).select_related(
            'reacted_by'
            )
    for post_reaction in post_reactions:
        post_details={
            'user_id':post_reaction.reacted_by_id,
            'name':post_reaction.reacted_by.name,
            'profile_pic':post_reaction.reacted_by.profile_pic,
            'reaction':post_reaction.reaction
        }
        post_reactions_details.append(post_details)

    return post_reactions_details



#Task-14

def get_user_posts(user_id):
    try:
        user_post_list=[]
        post_objs=Post.objects.select_related(
            'posted_by'
        ).prefetch_related(
            'post_reactions',
            Prefetch(
                'comments',
                to_attr='comments_on_post',
                queryset=Comment.objects.select_related(
                    'commented_by'    
                ).prefetch_related(
                    'comment_reactions'
                )
            )
        ).filter(posted_by_id=user_id)
        
        for post_obj in post_objs:
            post_details=get_post_details_from_post_object(post_obj)
            user_post_list.append(post_details)
    except User.DoesNotExist:
        raise InvalidUserException
    return user_post_list


#Task-15

def get_replies_for_comment(comment_id):
    try:
        comment_replies_list=[]
        comment_obj=Comment.objects.prefetch_related(
                Prefetch(
                    'reply_comments',
                    queryset=Comment.objects.select_related(
                        'commented_by'    
                    )
                )
            ).get(id=comment_id)
        for comment_reply in comment_obj.reply_comments.all():
            commenter={
                'user_id':comment_reply.commented_by.id,
                'name':comment_reply.commented_by.name,
                'profile_pic':comment_reply.commented_by.profile_pic
            }
            reply_detail={
                'comment_id':comment_reply.id,
                'commenter':commenter,
                'commented_at':str(comment_reply.commented_at)[0:26],
                'comment_content':comment_reply.content
            }
            comment_replies_list.append(reply_detail)
    except Comment.DoesNotExist:
        raise InvalidCommentException
    return comment_replies_list


#Task-13

def get_post(post_id):
    try:
        post_obj=Post.objects.select_related(
                'posted_by'
            ).prefetch_related(
                'post_reactions',
                Prefetch(
                    'comments',
                    to_attr='comments_on_post',
                    queryset=Comment.objects.select_related(
                        'commented_by'    
                    ).prefetch_related(
                        'comment_reactions'
                    )
                )
            ).get(id=post_id)
    except Post.DoesNotExist:
        raise InvalidPostException
    post_details=get_post_details_from_post_object(post_obj)
    return post_details


#To Get The user information

def get_user_details(user_obj):
    user_details={
        'user_id':user_obj.id,
        'name':user_obj.name,
        'profile_pic':user_obj.profile_pic
    }
    return user_details


#To Get Post Details From Post Object 

def get_post_details_from_post_object(post_obj):
    post_reaction_list,post_reaction_count=get_type_count_of_reaction_of_given_obj(post_obj.post_reactions.all())
    post_reactions={
        'count':post_reaction_count,
        'type':post_reaction_list
    }
    comments,comments_count=get_comments_for_a_post(post_obj)
    post_details={
        'post_id':post_obj.id,
        'posted_by':get_user_details(post_obj.posted_by),
        'posted_at':str(post_obj.posted_at)[0:26],
        'post_content':post_obj.content,
        'reactions':post_reactions,
        'comments':comments,
        'comments_count':comments_count
    }
    return post_details


#To Get comments on a post

def get_comments_for_a_post(post_obj):
    comments_details_list=[]
    comments_count=0
    for comment in post_obj.comments_on_post:
        if(not(comment.parent_comment_id)):
            reactions_list,reactions_count=get_type_count_of_reaction_of_given_obj(comment.comment_reactions.all())
            reactions={
                'count':reactions_count,
                'type':reactions_list
            }
            replies,replies_count=get_replies_for_comment_obj_with_reactions_and_replies(post_obj,comment)
            comment_info={
                'comment_id':comment.id,
                'commenter':get_user_details(comment.commented_by),
                'commented_at':str(comment.commented_at)[0:26],
                'comment_content':comment.content,
                'reactions':reactions,
                'replies_count':replies_count,
                'replies':replies
            }
            comments_count+=1
            comments_details_list.append(comment_info)
        
    return comments_details_list,comments_count



#To Get Replies for comment_objects with Reactions

def get_replies_for_comment_obj_with_reactions_and_replies(post_obj,comment_obj):
    comment_replies_list=[]
    replies_count=0
    for comment_reply_obj in post_obj.comments_on_post:
        if(
            comment_reply_obj.parent_comment_id == comment_obj.id 
            and
            comment_reply_obj.post_id==post_obj.id
            ):
            post_reactions_list,post_reactions_count=get_type_count_of_reaction_of_given_obj(
                    comment_reply_obj.comment_reactions.all()
                )
            reactions={
                'count':post_reactions_count,
                'type':post_reactions_list
            }
            reply_detail={
                'comment_id':comment_reply_obj.id,
                'commenter':get_user_details(comment_reply_obj.commented_by),
                'commented_at':str(comment_reply_obj.commented_at)[0:26],
                'comment_content':comment_reply_obj.content,
                'reactions':reactions
            }
            replies_count+=1
            comment_replies_list.append(reply_detail)
    return comment_replies_list,replies_count


# To Get Reaction Type and Count of When obj

def get_type_count_of_reaction_of_given_obj(reaction_objs):
    all_reactions_list=[]
    for reaction_obj in reaction_objs:
        all_reactions_list.append(reaction_obj.reaction)
    count=len(all_reactions_list)
    return list(set(all_reactions_list)),count
