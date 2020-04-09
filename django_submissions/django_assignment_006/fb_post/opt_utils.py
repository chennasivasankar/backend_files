from .models import *
from .models import *
import datetime
from .exceptions import *
from django.db.models import *
from django.db import *

# #def get_post(post_id):
#     post=Post.objects.select_related(
#             'posted_by'
#         ).prefetch_related(
#             'post_reactions'
#         ).prefetch_related(
#             Prefetch('comments',
#             queryset=Comment.objects.select_related(
#                     'commented_by'
#                 ).prefetch_related(
#                     'comment_reactions'
#                 )
#             ),
#             Prefetch(
#                 'comments',
#                 to_attr='comments_on_post',
#                 queryset=Comment.objects.filter(
#                     parent_comment__isnull=True
#                     ).select_related(
#                         'commented_by'
#                     ).prefetch_related(
#                         'comment_reactions'
#                     )
#             )
            
#         ).get(id=post_id)
#     return post


# post=Post.objects.prefetch_related(
#         Prefetch(
#                 'post_reactions',
#                 queryset=Reaction.objects.values_list('reaction')
#             )
#     ).get(id=2)

# #version-2
# post=Post.objects.select_related(
#             'posted_by'
#         ).prefetch_related(
#             'post_reactions'
#         ).prefetch_related(
#             Prefetch('comments',
#             queryset=Comment.objects.select_related(
#                     'commented_by'
#                 ).prefetch_related(
#                     'comment_reactions'
#                 )
#             ),
#             Prefetch(
#                 'comments',
#                 to_attr='comments_on_post',
#                 queryset=Comment.objects.filter(
#                     parent_comment__isnull=True
#                     ).select_related(
#                         'commented_by'
#                     ).prefetch_related(
#                         Prefetch(
#                             'comment_reactions',
#                             queryset=Comment.objects.select_related(
#                                     'parent_comment'
#                                 )
#                         )
#                     )
#             )
            
#         ).get(id=post_id)



# post=Post.objects.select_related(
#                 'posted_by'
#             ).prefetch_related(
#                 'post_reactions'
#             ).prefetch_related(
#                 Prefetch(
#                     'comments',
#                     to_attr='comments_on_post',
#                     queryset=Comment.objects.filter(
#                         parent_comment__isnull=True
#                         ).select_related(
#                             'commented_by'
#                         ).prefetch_related(
#                             Prefetch(
#                                 'comment_reactions',
#                             )
#                         ).prefetch_related(
#                             Prefetch(
#                                 'reply_comments',
#                                 queryset=Comment.objects.select_related(
#                                         'commented_by'
#                                     ).prefetch_related(
#                                         'comment_reactions'    
#                                     )
#                             )
#                         )
#                 )
#             ).get(id=post_id)
            
# user=User.objects.prefetch_related(
#         Prefetch(
#             'posts',
#             queryset=Post.objects.select_related(
#                 'posted_by'
#             ).prefetch_related(
#                 'post_reactions'
#             ).prefetch_related(
#                 Prefetch(
#                     'comments',
#                     to_attr='comments_on_post',
#                     queryset=Comment.objects.filter(
#                         parent_comment__isnull=True
#                         ).select_related(
#                             'commented_by'
#                         ).prefetch_related(
#                             Prefetch(
#                                 'comment_reactions',
#                             )
#                         ).prefetch_related(
#                             Prefetch(
#                                 'reply_comments',
#                                 queryset=Comment.objects.select_related(
#                                         'commented_by'
#                                     ).prefetch_related(
#                                         'comment_reactions'    
#                                     )
#                             )
#                         )
#                 )
#             )
        
#         )
#     ).get(id=user_id)


#Trail-Task-5

def react_to_post(user_id, post_id, reaction_type):
    user_objj = User.objects.filter(id = user_id)
    post_objj = Post.objects.filter(id = post_id)
    reaction_choice = [
            ('WOW'),
            ('LIT'),
            ('LOVE'),
            ('HAHA'),
            ('THUMBS-UP'),
            ('THUMBS-DOWN'),
            ('ANGRY'),
            ('SAD')
            ]
    reaction_objj = Reaction.objects.filter(post_id = post_id,reacted_by_id = user_id)
    if user_objj.exists():
        if post_objj .exists():
            if reaction_type in reaction_choice:
                if(reaction_objj and reaction_objj[0].reaction == reaction_type):
                    reaction_objj.delete()
                elif (reaction_objj and reaction_objj[0].reaction != reaction_type):
                    reaction_objj[0].reaction = reaction_type
                    reaction_objj[0].reacted_at = datetime.datetime.now()
                    reaction_objj[0].save()
                else:
                    Reaction.objects.create(post = Post(id = post_id),reaction = reaction_type,reacted_at = datetime.datetime.now(),reacted_by = User(id = user_id))
                    
                
            else:
                raise InvalidReactionTypeException
        else:
            raise InvalidPostException
            
    else:
          raise InvalidUserException
    

#Trail-Task-6

def react_to_comment(user_id, comment_id, reaction_type):
    user_objj = User.objects.filter(id = user_id)
    comment_objj = Comment.objects.filter(id = comment_id)
    reaction_objj = Reaction.objects.filter(comment_id = comment_id,reacted_by_id = user_id)
    reactions = [
            ('WOW'),
            ('LIT'),
            ('LOVE'),
            ('HAHA'),
            ('THUMBS-UP'),
            ('THUMBS-DOWN'),
            ('ANGRY'),
            ('SAD')
            ]
    if user_objj.exists():
        if comment_objj.exists():
            if reaction_type in reactions:
                if(reaction_objj and reaction_objj[0].reaction == reaction_type):
                    reaction_objj.delete()
                elif (reaction_objj and reaction_objj[0].reaction != reaction_type):
                    reaction_objj[0].reaction = reaction_type
                    reaction_objj[0].reacted_at = datetime.datetime.now()
                    reaction_objj[0].save()
                else:
                    Reaction.objects.create(comment = Comment(id = comment_id),reaction = reaction_type,reacted_at = datetime.datetime.now(),reacted_by = User(id = user_id))
            else:
                raise InvalidReactionTypeException
        else:
            raise InvalidCommentException
            
    else:
          raise InvalidUserException


#Task-13

def get_post(post_id):
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
    



#Success Task-13


#To Get The user information

# def get_user_details(user_obj):
#     user_details={
#         'user_id':user_obj.id,
#         'name':user_obj.name,
#         'profile_pic':user_obj.profile_pic
#     }
#     return user_details

# #To Get Post Details From Post Object
# def get_post_details_from_post_object(post_obj):
#     posted_by={
#         'name':post_obj.posted_by.name,
#         'user_id':post_obj.posted_by.id,
#         'profile_pic':post_obj.posted_by.profile_pic
#     }
#     post_reaction_list,post_reaction_count=get_type_count_of_reaction_of_given_obj(post_obj.post_reactions.all())
#     post_reactions={
#         'count':post_reaction_count,
#         'type':post_reaction_list
#     }
#     comments,comments_count=get_comments_for_a_post(post_obj)
#     post_details={
#         'post_id':post_obj.id,
#         'posted_by':posted_by,
#         'posted_at':str(post_obj.posted_at)[0:26],
#         'post_content':post_obj.content,
#         'reactions':post_reactions,
#         'comments':comments,
#         'comments_count':comments_count
#     }
#     return post_details


# #To Get comments on a post

# def get_comments_for_a_post(post_obj):
#     comments_details_list=[]
#     comments_count=0
#     for comment in post_obj.comments_on_post:
#         reactions_list,reactions_count=get_type_count_of_reaction_of_given_obj(comment.comment_reactions.all())
#         reactions={
#             'count':reactions_count,
#             'type':reactions_list
#         }
#         replies,replies_count=get_replies_for_comment_obj_with_reactions_and_replies(comment)
#         comment_info={
#             'comment_id':comment.id,
#             'commenter':get_user_details(comment.commented_by),
#             'commented_at':str(comment.commented_at)[0:26],
#             'comment_content':comment.content,
#             'reactions':reactions,
#             'replies_count':replies_count,
#             'replies':replies
#         }
#         comments_count+=1
#         comments_details_list.append(comment_info)
    
#     return comments_details_list,comments_count



# #To Get Replies for comment_objects with Reactions

# def get_replies_for_comment_obj_with_reactions_and_replies(comment_obj):
#     comment_replies_list=[]
#     replies_count=0
#     for comment_reply_obj in comment_obj.reply_comments.all():
#         commenter={
#             'user_id':comment_reply_obj.commented_by.id,
#             'name':comment_reply_obj.commented_by.name,
#             'profile_pic':comment_reply_obj.commented_by.profile_pic
#         }
#         post_reactions_list,post_reactions_count=get_type_count_of_reaction_of_given_obj(
#                 comment_reply_obj.comment_reactions.all()
#             )
#         reactions={
#             'count':post_reactions_count,
#             'type':post_reactions_list
#         }
#         reply_detail={
#             'comment_id':comment_reply_obj.id,
#             'commenter':commenter,
#             'commented_at':str(comment_reply_obj.commented_at)[0:26],
#             'comment_content':comment_reply_obj.content,
#             'reactions':reactions
#         }
#         replies_count+=1
#         comment_replies_list.append(reply_detail)
#     return comment_replies_list,replies_count


# # To Get Reaction Type and Count of When obj

# def get_type_count_of_reaction_of_given_obj(reaction_objs):
#     all_reactions_list=[]
#     for reaction_obj in reaction_objs:
#         all_reactions_list.append(reaction_obj.reaction)
#     count=len(all_reactions_list)
#     return list(set(all_reactions_list)),count
    

# #Task-13
# def get_post(post_id):
#     try:
#         post=Post.objects.select_related(
#                 'posted_by'
#             ).prefetch_related(
#                 'post_reactions'
#             ).prefetch_related(
#                 Prefetch(
#                     'comments',
#                     to_attr='comments_on_post',
#                     queryset=Comment.objects.filter(
#                         parent_comment__isnull=True
#                         ).select_related(
#                             'commented_by'
#                         ).prefetch_related(
#                             Prefetch(
#                                 'comment_reactions',
#                             )
#                         ).prefetch_related(
#                             Prefetch(
#                                 'reply_comments',
#                                 queryset=Comment.objects.select_related(
#                                         'commented_by'
#                                     ).prefetch_related(
#                                         'comment_reactions'    
#                                     )
#                             )
#                         )
#                 )
#             ).get(id=post_id)
#     except Post.DoesNotExist:
#         raise InvalidPostException
        
#     post_details=get_post_details_from_post_object(post_obj=post)
#     return post_details

