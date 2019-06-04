import json

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from EventCenter.managers import channel_manager
from EventCenter.responses import error_json_response, success_json_response
from EventCenter.serializers import channel_list_serializer, channel_serializer
from EventCenter.views.view_decorators import admin_required


@login_required
@csrf_exempt
def channel_list(request):
    if request.method == 'GET':
        return view_channel_list(request)

    elif request.method == 'POST':
        return create_channel(request)

    elif request.method == 'PUT':
        return edit_channel(request)

    elif request.method == 'DELETE':
        return delete_channel(request)

    return error_json_response('No such API')


def view_channel_list(request):
    args = request.GET
    try:
        offset = int(args.get('offset', 0))
        limit = int(args.get('limit', 10))
    except ValueError:
        return error_json_response('Invalid arguments')

    channels = channel_manager.all_channels().order_by('-id')[offset:offset + limit]
    return success_json_response({'channels': channel_list_serializer(channels),
                                  'count': channel_manager.count()})


@admin_required
def create_channel(request):
    try:
        data = json.loads(request.body)
        validation = channel_manager.is_valid_channel(data)
        if not validation['state']:
            return error_json_response(validation['error'])

        channel = channel_manager.create_channel(data)
    except ValueError:
        return error_json_response('Invalid JSON file')
    except (KeyError, TypeError):
        return error_json_response('Invalid arguments')

    return success_json_response({'channel': channel_serializer(channel)})


@admin_required
def edit_channel(request):
    try:
        data = json.loads(request.body)
        channel_id = data['id']
        if not channel_manager.is_channel_exists(channel_id):
            return error_json_response('No such channel')

        validation = channel_manager.is_valid_channel(data)
        if not validation['state']:
            return error_json_response(validation['error'])

        channel = channel_manager.update_channel(channel_id, data)

    except ValueError:
        return error_json_response('Invalid JSON file')
    except (KeyError, TypeError):
        return error_json_response('Invalid / Missing arguments')

    return success_json_response({'channel': channel_serializer(channel)})


@admin_required
def delete_channel(request):
    try:
        data = json.loads(request.body)
        channel_id = data['id']
        if not channel_manager.is_channel_exists(channel_id):
            return error_json_response('No such channel')

        channel_manager.delete_channel(channel_id)

    except ValueError:
        return error_json_response('Invalid JSON file')
    except (KeyError, TypeError):
        return error_json_response('Invalid / Missing arguments')

    return success_json_response({'message': 'Channel Successfully deleted'})


