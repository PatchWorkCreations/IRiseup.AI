from django.urls import path
from . import views


urlpatterns = [
    path('', views.CustomLoginView.as_view(), name='custom_login'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Use the function-based view
    path('courses/', views.course_list, name='course_list'),
    path('user-management/', views.user_management, name='user_management'),
    path('courses/add/', views.add_course, name='add_course'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('courses/<int:course_id>/edit/', views.edit_course, name='edit_course'),
    path('courses/<int:course_id>/delete/', views.delete_course, name='delete_course'),
    path('customadmin/courses/<int:pk>/delete/', views.delete_course, name='delete_course'),
    path('sub_courses/add/', views.add_sub_course, name='add_sub_course'),
    path('sub_courses/<int:sub_course_id>/edit/', views.edit_sub_course, name='edit_sub_course'),
    path('lessons/add/', views.add_lesson, name='add_lesson'),
    path('lessons/<int:lesson_id>/edit/', views.edit_lesson, name='edit_lesson'),
    path('logout/', views.CustomLogoutView.as_view(), name='custom_logout'),
    path('upload-csv/', views.upload_csv, name='upload_csv'),
    path('send-password-reset/<int:user_id>/', views.send_password_reset, name='send_password_reset'),
    path('user-management/edit/<int:user_id>/', views.edit_user, name='customadmin_edit_user'),
    path('delete-user/<int:item_id>/', views.delete_user, name='delete_user'),
    path('user-management/', views.user_management, name='user_management'),
    path('view-user-quiz-details/<int:user_id>/', views.view_user_quiz_details, name='customadmin_view_user_quiz_details'),
    path('delete-multiple-users/', views.delete_multiple_users, name='delete_multiple_users'),

    path('manage-knowledge-base/', views.manage_knowledge_base, name='manage_knowledge_base'),
    path('add-subcategory/', views.add_subcategory, name='add_subcategory'),
    path('edit-subcategory/<int:id>/', views.edit_subcategory, name='edit_subcategory'),
    path('add-category/', views.add_category, name='add_category'),
    path('edit-category/<int:id>/', views.edit_category, name='edit_category'),
    path('add-article/', views.add_article, name='add_article'),
    path('edit-article/<int:id>/', views.edit_article, name='edit_article'),

    path('delete-category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('delete-subcategory/<int:id>/', views.delete_subcategory, name='delete_subcategory'),
    path('delete-article/<int:article_id>/', views.delete_article, name='delete_article'),

    path('download-transactions-csv/', views.download_transactions_csv, name='download_transactions_csv'),
    path('view-transactions/', views.view_transactions, name='view_transactions'),
    path('transactions/', views.customadmin_transactions, name='customadmin_transactions'),  # No customadmin prefix
    

    path('sub_courses/<int:sub_course_id>/delete/', views.delete_sub_course, name='delete_sub_course'),
    path('lessons/<int:lesson_id>/delete/', views.delete_lesson, name='delete_lesson'),

    path('sub-course/<int:sub_course_id>/update-order/', views.update_sub_course_order, name='update_sub_course_order'),
    path('lesson/<int:lesson_id>/update-order/', views.update_lesson_order, name='update_lesson_order'),
    
    path('add-blog/', views.add_blog, name='add_blog'),  # Ensure this matches
    path('blogs/', views.blog_list, name='blog_list'),   # This should also match
    path('blogs/edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('blogs/delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),

    path('reorder-courses/', views.reorder_courses, name='reorder_courses'),
    path('customadmin/courses/<int:pk>/toggle/', views.toggle_course_status, name='toggle_course'),
]
