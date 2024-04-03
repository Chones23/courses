import frappe
from courses.chart import generate_radar_chart
import hashlib

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

def get_categories_key():
    doc = frappe.get_doc("DocType", "Advanced Class Module 1 Preliminary Assessment")
    
    categories_key = [  [], [], [],
                        [], [], [],
                        [], [], [],
                        [], [], []  ]
    index = -1

    for i in doc.fields:
        if i.fieldtype == "Section Break":
            for j in categories:
                if (i.label):
                    if i.label.lower() == j.lower():
                        index += 1
                        break
        elif index >= 0 and index < len(categories_key) and i.fieldtype == "Select" and "Setuju" in i.options:
            categories_key[index].append(i.fieldname)
    
    return categories_key


def execute(doc, method):
    categories_key = get_categories_key()
    
    categories_values = [   0, 0, 0,
                            0, 0, 0,
                            0, 0, 0,
                            0, 0, 0 ]
    index = 0
    for category_key in categories_key:
        for key in category_key:
            category = getattr(doc, key, '')
            if category == "Setuju" or category == "Sangat Setuju":
                categories_values[index] += 1
        index += 1
    print(categories_values)
    print('test')
    fig = generate_radar_chart(categories, categories_values)
    salt = hashlib.md5("{}{}{}".format(doc.name, doc.owner, doc.creation)).hexdigest()
    final_filepath = '{}/sites/{}/public/files/pre-test-{}.png'.format(frappe.utils.get_bench_path(), frappe.utils.get_site_path().replace('./',''), salt)
    fig.write_image(final_filepath)

    doc.chart_image = "/files/pre-test-{}.png".format(salt)