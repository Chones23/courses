# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "courses"
app_title = "Courses"
app_publisher = "Nusantara Digital Konsultan"
app_description = "App for Courses"
app_icon = "fa fa-certificate"
app_color = "#DE3163"
app_email = "develop@ridhosribumi.co"
app_license = "Nusantara Digital Konsultan"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/courses/css/courses.css"
# app_include_js = "/assets/courses/js/courses.js"

# include js, css files in header of web template
# web_include_css = "/assets/courses/css/courses.css"
# web_include_js = "/assets/courses/js/courses.js"

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
# get_website_user_home_page = "courses.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "courses.install.before_install"
# after_install = "courses.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "courses.notifications.get_notification_config"

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
	"Advanced Class Module 1 Preliminary Assessment": {
		"validate": [
			"courses.doc_events.advanced_class_module_1_preliminary_assessment.generate_plotlib_radar_chart.execute",
			"courses.doc_events.advanced_class_module_1_preliminary_assessment.generate_hasil_review.execute"
		]
	},
	"Advanced Class Module 8 Post Learning Assessment": {
		"validate": [
			"courses.doc_events.advanced_class_module_8_post_learning_assessment.generate_plotlib_radar_chart.execute",
			"courses.doc_events.advanced_class_module_8_post_learning_assessment.generate_hasil_review.execute"
		]
	}
}


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"courses.tasks.all"
# 	],
# 	"daily": [
# 		"courses.tasks.daily"
# 	],
# 	"hourly": [
# 		"courses.tasks.hourly"
# 	],
# 	"weekly": [
# 		"courses.tasks.weekly"
# 	]
# 	"monthly": [
# 		"courses.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "courses.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "courses.event.get_events"
# }
