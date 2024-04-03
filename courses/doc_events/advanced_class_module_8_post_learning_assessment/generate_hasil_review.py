import frappe
from courses.doc_events.advanced_class_module_8_post_learning_assessment.generate_plotlib_radar_chart import get_categories_key

categories = [  'Spiritual', 
                'Kesehatan dan Kebugaran Tubuh', 
                'Intelektualitas', 
                'Emosional', 
                'Karakter', 
                'Asmara dan Cinta', 
                'Parenting', 
                'Sosial', 
                'Finansial', 
                'Karir', 
                'Kualitas Hidup Anda',
                'Visi Kehidupan']


def execute(doc, method):
    categories_key = get_categories_key()
    index = 0
    hasil_review = ''
    for category_key in categories_key:
        value = 0
        for key in category_key:
            category = getattr(doc, key, '')
            if category == "Setuju" or category == "Sangat Setuju":
                value += 1
        hasil_review += "{}={}\n".format(categories[index], value)
        index+=1
    
    doc.hasil_review = hasil_review