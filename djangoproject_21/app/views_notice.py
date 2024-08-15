from django.shortcuts import render, redirect
from app.models import user
from notifications.signals import notify


def send_notifications(sender, verb, receiver, target=None,
                       description=None, **kwargs):
    """
        sender(发件人): 任何类型的对象。（必需）如果打算使用关键字参数，要使用sender
        receiver(收件人): 一组或一个用户查询集或列表的用户（必需的）
        verb(动作): 一个字符串（必需的）
        target(目标): 任何类型的对象（可选的）
        level(等级): Notification.LEVELS ('success', 'info', 'warning', 'error') 之一（可选的）
        description(描述): 一个字符串（可选的）
        public(公共的): 一个布尔值（默认值=True）（可选的）
        timestamp(时间戳)
    """
    recipients = user.objects.filter(userClass=receiver)
    # recipients = user.objects.all()
    for recipient in recipients:
        notify.send(sender=sender,
                    recipient=recipient,
                    verb=verb,
                    target=target,
                    description=description,
                    **kwargs
                    )


def get_unread_notifications(request):
    # 获取未读消息列表
    print('[USER]', request.user)
    unread_notifications = request.user.notifications.unread()
    return render(request, 'notifications_unread.html', {'unread_list': unread_notifications})


def get_read_notifications(request):
    # 获取已读消息列表
    print('[USER]', request.user)
    read_notifications = request.user.notifications.read()
    return render(request, 'notifications_read.html', {'read_list': read_notifications})


# 更新通知状态
def update_status(request):
    notice_id = request.GET.get('notice_id')
    # 更新单条通知
    if notice_id:
        request.user.notifications.get(id=notice_id).mark_as_read()
        return redirect('get_unread_notifications')
    # 更新全部通知
    else:
        request.user.notifications.mark_all_as_read()
        return redirect('get_unread_notifications')
