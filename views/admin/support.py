##
#    Copyright (C) 2013 Jessica Tallon & Matt Molyneaux
#   
#    This file is part of Inboxen front-end.
#
#    Inboxen front-end is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Inboxen front-end is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with Inboxen front-end.  If not, see <http://www.gnu.org/licenses/>.
##

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from website.models import Email, Alias


@login_required
@staff_member_required
def support(request, page=1):
    alias = Alias.objects.filter(alias="support")
    emails = []
    for a in alias:
        emails += list(Email.objects.filter(inbox=a).order_by('-recieved_date'))
    
    paginator = Paginator(emails, 100)
    try:
        emails = paginator.page(page)
    except PageNotAnInteger:
        emails = paginator.page(1)
    except EmptyPage:
        emails = paginator.page(paginator.num_pages)

    for email in emails.object_list:
        email.sender, email.subject = "", "(No Subject)"
        for header in email.headers.all():
            if header.name == "From":
                email.sender = header.data
            elif header.name == "Subject":
                email.subject = header.data

    context = {
        "page":"Support Inbox",
        "emails":emails,
    }

    return render(request, "admin/support.html", context)
