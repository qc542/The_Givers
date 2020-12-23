from models import NewsFeedPost
import sys
from app import db
from utils import testData
import json

def addNewsfeedPost(title, body, api_params, api_links, org_id):
    newPost = NewsFeedPost(title=title, body=body, api_params=api_params, \
            api_links=api_links, org_id=org_id)
    try:
        db.session.add(newPost)
        db.session.commit()        
        return 1
    except IntegrityError as e:
        print(e.__dict__)
        return "Failed to add post to database"

# Get all news feed posts belonging to an organization by providing the org_id
def getNewsfeedPosts(org_id):
    result = NewsFeedPost.query.filter_by(org_id=org_id)
    if result == None:
        return "No posts are associated with this charity"
    transformedPosts = []
    for post in result:
        transformedPost = NewsFeedPost(title=post.title, body=post.body, \
                api_params=post.api_params, api_links=post.api_links, \
                org_id=post.org_id).__repr__()
        transformedPosts.append(transformedPost)
    return transformedPosts
