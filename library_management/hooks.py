 app_name = "library_management"
app_title = "Library Management"
app_publisher = "mohamed khalid"
app_description = "library management system"
app_icon = "icon-book"
app_color = "#589494"
app_email = "mk5086944@gmail.com"


role_home_page = {
	"Library Member": "article"
}


scheduler_events = {
	"daily": [
		"library_management.tasks.daily"
	],
}
