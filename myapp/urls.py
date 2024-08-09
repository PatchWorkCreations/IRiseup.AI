from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog-classic/', views.blogclassic, name='blogclassic'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('index-2/', views.index2, name='index2'),
    path('index-3/', views.index3, name='index3'),
    path('login/', views.login, name='login'),
    path('news-detail/', views.newsdetail, name='newsdetail'),
    path('not-found/', views.notfound, name='notfound'),
    path('pricing/', views.pricing, name='pricing'),
    path('register/', views.register, name='register'),
    path('reset/', views.reset, name='reset'),
    path('service-detail/', views.servicedetail, name='servicedetail'),
    path('services/', views.services, name='services'),
    path('team-detail/', views.teamdetail, name='teamdetail'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('news-detail1/', views.newsdetail1, name='newsdetail1'),
    path('news-detail2/', views.newsdetail2, name='newsdetail2'),
    path('news-detail3/', views.newsdetail3, name='newsdetail3'),
    path('news-detail4/', views.newsdetail4, name='newsdetail4'),
    path('news-detail5/', views.newsdetail5, name='newsdetail5'),
    path('news-detail6/', views.newsdetail6, name='newsdetail6'),
    path('news-detail7/', views.newsdetail7, name='newsdetail7'),
    path('news-detail8/', views.newsdetail8, name='newsdetail8'),
    path('service-detail1/', views.servicedetail1, name='servicedetail1'),
    path('service-detail2/', views.servicedetail2, name='servicedetail2'),
    path('service-detail3/', views.servicedetail3, name='servicedetail3'),
    path('service-detail4/', views.servicedetail4, name='servicedetail4'),
    path('service-detail5/', views.servicedetail5, name='servicedetail5'),
    path('coursemenu/', views.coursemenu, name='coursemenu'),

    path('sub_courses/<int:sub_course_id>/', views.sub_course_detail, name='sub_course_detail'),
    path('lessons/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('lessons/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('lessons/<int:lesson_id>/next/', views.next_lesson, name='next_lesson'),


    path('start_quiz/', views.start_quiz, name='start_quiz'),
    path('age_selection/', views.age_selection, name='age_selection'),

    path('after-age/', views.after_age_page, name='after_age_page'),

    path('main_goal/', views.main_goal, name='main_goal'),
    path('income_source/', views.income_source, name='income_source'),
    path('work_schedule/', views.work_schedule, name='work_schedule'),
    path('job_challenges/', views.job_challenges, name='job_challenges'),

    path('after-job-challenges/', views.after_job_challenges_page, name='after_job_challenges_page'),
    
    path('financial_situation/', views.financial_situation, name='financial_situation'),

    path('comfortable-financial/', views.comfortable_financial, name='comfortable_financial'),
    path('stability-financial/', views.stability_financial, name='stability_financial'),
    path('struggling-financial/', views.struggling_financial, name='struggling_financial'),
    
    path('annual-income-goal/', views.annual_income_goal, name='annual_income_goal'),
    path('control-work-hours/', views.control_work_hours, name='control_work_hours'),
    path('routine-work/', views.routine_work, name='routine_work'),
    path('time-saved-use/', views.time_saved_use, name='time_saved_use'),


    path('job-interest-question/', views.job_interest_question, name='job_interest_question'),
    path('job_interest_match/', views.job_interest_match, name='job_interest_match'),

    path('absolutely-interest/', views.absolutely_interest, name='absolutely_interest'),
    path('somewhat-interest/', views.somewhat_interest, name='somewhat_interest'),
    path('maybe-interest/', views.maybe_interest, name='maybe_interest'),
    path('not-necessarily-interest/', views.not_necessarily_interest, name='not_necessarily_interest'),
    

    path('digital_business_knowledge/', views.digital_business_knowledge, name='digital_business_knowledge'),
    path('side_hustle_experience/', views.side_hustle_experience, name='side_hustle_experience'),
    path('learning_new_skills/', views.learning_new_skills, name='learning_new_skills'),
    path('ai_tools_familiarity/', views.ai_tools_familiarity, name='ai_tools_familiarity'),
    path('content_writing_knowledge/', views.content_writing_knowledge, name='content_writing_knowledge'),
    path('digital_marketing_knowledge/', views.digital_marketing_knowledge, name='digital_marketing_knowledge'),
    path('ai_income_boost_awareness/', views.ai_income_boost_awareness, name='ai_income_boost_awareness'),
    path('fields_interest/', views.fields_interest, name='fields_interest'),
    path('ai_mastery_readiness/', views.ai_mastery_readiness, name='ai_mastery_readiness'),

    path('all-set/', views.all_set, name='all_set'),
    path('ready/', views.ready, name='ready'),
    path('somewhat-ready/', views.somewhat_ready, name='somewhat_ready'),
    path('not-ready/', views.not_ready, name='not_ready'),
    
    path('focus_ability/', views.focus_ability, name='focus_ability'),
    path('special_goal/', views.special_goal, name='special_goal'),
    path('time_to_achieve_goal/', views.time_to_achieve_goal, name='time_to_achieve_goal'),
    path('summary/', views.summary, name='summary'),
    path('results/', views.results, name='results'),


]
