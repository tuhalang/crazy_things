import json
import os
import csv


CONTEXT_PATH_MSG = '/home/tuhalang/Downloads/FacebookMining/data/messages/inbox'
MSG_FILE_NAME = 'message_1.json'
MY_NAME = 'Hung Pham'

CONTEXT_PATH_STORIES = '/home/tuhalang/Downloads/FacebookMining/data/stories'
REACT_STORIES_NAME = 'story_reactions.json'
ARCHIVED_STORIES_NAME = 'archived_stories.json'

CONTEXT_PATH_FRIENDS = '/home/tuhalang/Downloads/FacebookMining/data/friends'
FRIEND_NAME = 'friends.json'
REJECTED_NAME = 'rejected_friend_requests.json'
REMOVED_NAME = 'removed_friends.json'
SENT_NAME = 'sent_friend_requests.json'

CONTEXT_PATH_COMMENTS = '/home/tuhalang/Downloads/FacebookMining/data/comments'
COMMENTS_NAME = 'comments.json'

CONTEXT_PATH_POSTS = '/home/tuhalang/Downloads/FacebookMining/data/posts'
POSTS_NAME = 'your_posts_1.json'

def write(data, file_name):
    with open(file_name, mode="a") as marks_file:
        file_writer = csv.writer(
            marks_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        file_writer.writerow(data)


def analysisCmtAndPost():
    comments_path = os.path.join(CONTEXT_PATH_COMMENTS, COMMENTS_NAME)
    posts_path = os.path.join(CONTEXT_PATH_POSTS, POSTS_NAME)

    comments_file = open(comments_path)
    posts_file = open(posts_path)

    comments_data = json.load(comments_file)
    posts_data = json.load(posts_file)

    num_comments = len(comments_data['comments'])
    num_posts = len(posts_data)

    data = []
    data.append(str(num_comments))
    data.append(str(num_posts))

    write(data, 'posts.csv')

    comments_file.close()
    posts_file.close()

def analysisFriend():
    friends_path = os.path.join(CONTEXT_PATH_FRIENDS, FRIEND_NAME)
    rejected_path = os.path.join(CONTEXT_PATH_FRIENDS, REJECTED_NAME)
    removed_path = os.path.join(CONTEXT_PATH_FRIENDS, REMOVED_NAME)
    sent_path = os.path.join(CONTEXT_PATH_FRIENDS, SENT_NAME)

    friends_file = open(friends_path)
    rejected_file = open(rejected_path)
    removed_file = open(removed_path)
    sent_file = open(sent_path)

    friends_data = json.load(friends_file)
    rejected_data = json.load(rejected_file)
    removed_data = json.load(removed_file)
    sent_data = json.load(sent_file)

    num_friends = len(friends_data['friends'])
    num_rejected = len(rejected_data['rejected_requests'])
    num_removed = len(removed_data['deleted_friends'])
    num_sent = len(sent_data['sent_requests'])

    data = []
    data.append(str(num_friends))
    data.append(str(num_rejected))
    data.append(str(num_removed))
    data.append(str(num_sent))

    write(data, 'friends.csv')

    friends_file.close()
    rejected_file.close()
    removed_file.close()
    sent_file.close()


def analysisMsg():
    paths = os.listdir(CONTEXT_PATH_MSG)
    for path in paths:
        json_path = os.path.join(CONTEXT_PATH_MSG, path, MSG_FILE_NAME)
        msg_file = open(json_path)
        data = json.load(msg_file)
        messages = data['messages']
        count_me = 0
        count_other = 0
        for msg in messages:
            if msg['sender_name'].encode('latin1').decode('utf8') == MY_NAME:
                count_me += 1
            else:
                count_other += 1
        
        data = []
        data.append(path)
        data.append(str(len(messages)))
        data.append(str(count_me))
        data.append(str(count_other))

        write(data, 'msg.csv')
        msg_file.close()

def analysisStories():
    react_stories_path = os.path.join(CONTEXT_PATH_STORIES, REACT_STORIES_NAME)
    react_stories_file = open(react_stories_path)
    data = json.load(react_stories_file)

    liked = 0
    loved = 0
    wowed = 0
    angry = 0
    haha = 0
    sad = 0
    reacted = 0

    feedbacks = data['stories_feedback']
    for feedback in feedbacks:
        title = feedback['title']
        if title.find('liked') >= 0:
            liked += 1
        if title.find('loved') >= 0:
            loved += 1
        if title.find('wowed') >= 0:
            wowed += 1
        if title.find('angry') >= 0:
            angry += 1
        if title.find('haha') >= 0:
            haha += 1
        if title.find('sad') >= 0:
            sad += 1
        if title.find('reacted') >= 0:
            reacted += 1
    
    data = []
    data.append(str(liked))
    data.append(str(loved))
    data.append(str(wowed))
    data.append(str(angry))
    data.append(str(haha))
    data.append(str(sad))
    data.append(str(reacted))

    write(data, 'stories.csv')

    react_stories_file.close()

analysisCmtAndPost()
