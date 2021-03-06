# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "hr_customizations"
app_title = "Attendance Request changes"
app_publisher = "STS"
app_description = "Attendance Request changes"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "rajat@example.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hr_customizations/css/hr_customizations.css"
# app_include_js = "/assets/hr_customizations/js/hr_customizations.js"

# include js, css files in header of web template
# web_include_css = "/assets/hr_customizations/css/hr_customizations.css"
# web_include_js = "/assets/hr_customizations/js/hr_customizations.js"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "hr_customizations.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "hr_customizations.install.before_install"
# after_install = "hr_customizations.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hr_customizations.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Attendance Request": {
		"before_validate": "hr_customizations.attendance_request_changes.future_attendance_request.validate",
	},
	"Attendance": {
		"before_validate": "hr_customizations.attendance_request_changes.mark_future_attendance.validate",
	},
	"Leave Application": {
		"before_validate": "hr_customizations.attendance_request_changes.leave_application_validate.abc",
		"validate":"hr_customizations.attendance_request_changes.leave_application_validate.validate",
		"before_save": "hr_customizations.attendance_request_changes.leave_approver_fix.on_update",
	    "before_submit": "hr_customizations.attendance_request_changes.leave_approver_fix.validate",
	},
	"Leave Allocation":{
		"on_submit": "hr_customizations.attendance_request_changes.leave_allocation.allocate_earned_leaves",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"hr_customizations.tasks.all"
# 	],
# 	"daily": [
# 		"hr_customizations.tasks.daily"
# 	],
# 	"hourly": [
# 		"hr_customizations.tasks.hourly"
# 	],
# 	"weekly": [
# 		"hr_customizations.tasks.weekly"
# 	]
# 	"monthly": [
# 		"hr_customizations.tasks.monthly"
# 	]
# }

scheduler_events = {
    "cron": {
    	"30 11 * * *":[
    		"attendance_request_changes.leave_allocation.allocate_earned_leaves_cron"
    	]
    }
}

# Testing
# -------

# before_tests = "hr_customizations.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hr_customizations.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "hr_customizations.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

