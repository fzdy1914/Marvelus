import json

from django.views.decorators.csrf import csrf_exempt

from luminus.managers import forum_manager
from luminus.responses import success_json_response, error_json_response
from luminus.view_decorators import json_request


def get_viewable_forum(request, code):
    user = request.user
    if request.user.is_authenticated:
        uname = user.uname
        forums = forum_manager.get_forum_by_code_and_uname(code, uname)
        return success_json_response({'forums': forums})
    return error_json_response("User not logged in")


def get_forum_by_code(request, code):
    forums = forum_manager.get_forum_by_code(code)
    return success_json_response({'forums': forums})


def get_forum_by_code_and_group_num(request, code, group_num):
    forums = forum_manager.get_forum_by_code_and_group_num(code, group_num)
    return success_json_response({'forums': forums})


def get_forum_notintut_by_code_and_group_num(request, code, group_num):
    forums = forum_manager.get_forum_notintut_by_code_and_group_num(code, group_num)
    return success_json_response({'forums': forums})


def add_forum_to_tut_by_code_group_num_fid(request, code, group_num, fid):
    forum = forum_manager.add_forum_to_tut_by_code_group_num_fid(code, group_num, fid)
    return success_json_response({'forum': forum})


def delete_forum(request, code, fid):
    forum_manager.delete_forum(code, fid)
    return success_json_response({})


@json_request
@csrf_exempt
def add_forum(request):
    user = request.user
    if user.is_authenticated:
        data = json.loads(request.body)
        forum_manager.add_reply(data['code'], data['title'])
        return success_json_response({})
    return error_json_response("User not logged in")
