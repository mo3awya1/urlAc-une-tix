import csv

# قراءة الروابط من ملف نصي
input_file = 'domin.txt'  # اسم الملف الذي يحتوي على الروابط
output_file = 'formatted_urls.csv'  # اسم الملف لحفظ النتيجة بصيغة CSV

# قراءة الروابط من الملف
with open(input_file, 'r') as infile:
    urls = [line.strip() for line in infile if line.strip()]  # إزالة الفراغات الزائدة

# إنشاء قائمة من الروابط مكررة في كل سطر
formatted_urls = [f"{url}, {url}" for url in urls]

# طباعة النتيجة (اختياري)
for url in formatted_urls:
    print(url)

# حفظ النتيجة في ملف CSV
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for url in formatted_urls:
        writer.writerow([url])

print(f"تم حفظ الروابط المدمجة في الملف: {output_file}")
