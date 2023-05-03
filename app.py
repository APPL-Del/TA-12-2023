from flask import Flask
import pickle
import pandas as pd
from flask import render_template, request

app = Flask(__name__)

with open('modelSvm.pkl', 'rb') as model:
  svm_model = pickle.load(model)

with open('modelSvmPso.pkl', 'rb') as model:
  svmpso_model = pickle.load(model)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/svm')
def svm():
    return render_template('svm.html')
@app.route('/svmpso')
def svmpso():
    return render_template('svmpso.html')

@app.route('/svmpredict', methods=['POST'])
def svmpredict():
   data = {
        'jumlah_anggota_rumah_tangga' : [request.form["jumlah_anggota_rumah_tangga"]],
        'jumlah_kamar' : [request.form["jumlah_kamar"]],
        'jumlah_sapi' : [request.form["jumlah_sapi"]],
        'jumlah_kerbau' : [request.form["jumlah_kerbau"]],
        'jumlah_kuda' : [request.form["jumlah_kuda"]],
        'jumlah_kambing' : [request.form["jumlah_kambing"]],
        'jumlah_babi' : [request.form["jumlah_babi"]],
        'status_kredit_usaha_rakyat_Tidak' : [request.form["status_kredit_usaha_rakyat"]],
        'status_kredit_usaha_rakyat_Ya' : [request.form["status_kredit_usaha_rakyat"]],
        'status_rastra_Tidak' : [request.form["status_rastra"]],
        'status_rastra_Ya' : [request.form["status_rastra"]],
        'status_jamsostek_Tidak' : [request.form["status_jamsostek"]],
        'status_jamsostek_Ya' : [request.form["status_jamsostek"]],
        'status_asuransi_Tidak' : [request.form["status_asuransi"]],
        'status_asuransi_Ya' : [request.form["status_asuransi"]],
        'status_bpjs_mandiri_Tidak' : [request.form["status_bpjs_mandiri"]],
        'status_bpjs_mandiri_Ya' : [request.form["status_bpjs_mandiri"]],
        'status_kis_Tidak' : [request.form["status_kis"]],
        'status_kis_Ya' : [request.form["status_kis"]],
        'status_kip_Tidak' : [request.form["status_kip"]],
        'status_kip_Ya' : [request.form["status_kip"]],
        'status_kks_Tidak' : [request.form["status_kks"]],
        'status_kks_Ya' : [request.form["status_kks"]],
        'status_usaha_art_Tidak' : [request.form["status_usaha_art"]],
        'status_usaha_art_Ya' : [request.form["status_usaha_art"]],
        'ada_kapal_Tidak' : [request.form["ada_kapal"]],
        'ada_kapal_Ya' : [request.form["ada_kapal"]],
        'ada_perahu_Tidak' : [request.form["ada_perahu"]],
        'ada_perahu_Ya' : [request.form["ada_perahu"]],
        'ada_mobil_Tidak' : [request.form["ada_mobil"]],
        'ada_mobil_Ya' : [request.form["ada_mobil"]],
        'ada_motor_Tidak' : [request.form["ada_motor"]],
        'ada_motor_Ya' : [request.form["ada_motor"]],
        'ada_sepeda_Tidak' : [request.form["ada_sepeda"]],
        'ada_sepeda_Ya' : [request.form["ada_sepeda"]],
        'ada_laptop_Tidak' : [request.form["ada_laptop"]],
        'ada_laptop_Ya' : [request.form["ada_laptop"]],
        'ada_emas_Tidak' : [request.form["ada_emas"]],
        'ada_emas_Ya' : [request.form["ada_emas"]],
        'ada_tv_Tidak' : [request.form["ada_tv"]],
        'ada_tv_Ya' : [request.form["ada_tv"]],
        'ada_telepon_Tidak' : [request.form["ada_telepon"]],
        'ada_telepon_Ya' : [request.form["ada_telepon"]],
        'ada_pemanas_Tidak' : [request.form["ada_pemanas"]],
        'ada_pemanas_Ya' : [request.form["ada_pemanas"]],
        'ada_ac_Tidak' : [request.form["ada_ac"]],
        'ada_ac_Ya' : [request.form["ada_ac"]],
        'ada_lemari_es_Tidak' : [request.form["ada_lemari_es"]],
        'ada_lemari_es_Ya' : [request.form["ada_lemari_es"]],
        'ada_tabung_gas_Tidak' : [request.form["ada_tabung_gas"]],
        'ada_tabung_gas_Ya' : [request.form["ada_tabung_gas"]],
        'kepemilikan_rumah_Bebas Sewa' : 0,
        'kepemilikan_rumah_Dinas' : 0,
        'kepemilikan_rumah_Kontrak' : 0,
        'kepemilikan_rumah_Lainnya' : 0,
        'kepemilikan_rumah_Milik Sendiri' : 0,
        'kepemilikan_lahan_Lainnya' : 0,
        'kepemilikan_lahan_Milik Orang Lain' : 0,
        'kepemilikan_lahan_Milik Sendiri' : 0,
        'kepemilikan_lahan_Tanah Negara' : 0,
        'jenis_lantai_Bambu' : 0,
        'jenis_lantai_Bata Merah' : 0,
        'jenis_lantai_Kayu' : 0,
        'jenis_lantai_Keramik' : 0,
        'jenis_lantai_Lainnya' : 0,
        'jenis_lantai_Marmer' : 0,
        'jenis_lantai_Parket' : 0,
        'jenis_lantai_Tanah' : 0,
        'jenis_lantai_Ubin' : 0,
        'jenis_dinding_Anyaman Bambu': 0,
        'jenis_dinding_Bambu': 0,
        'jenis_dinding_Batang Kayu': 0,
        'jenis_dinding_Kayu': 0,
        'jenis_dinding_Lainnya': 0,
        'jenis_dinding_Plesteran': 0,
        'jenis_dinding_Tembok': 0,
        'jenis_atap_Asbes': 0,
        'jenis_atap_Bambu': 0,
        'jenis_atap_Beton': 0,
        'jenis_atap_Genteng Keramik': 0,
        'jenis_atap_Lainnya': 0,
        'jenis_atap_Seng': 0,
        'jenis_atap_Sirap': 0,
        'sumber_air_minum_Air Hujan': 0,
        'sumber_air_minum_Air Isi Ulang': 0,
        'sumber_air_minum_Air Kemasan Bermerk': 0,
        'sumber_air_minum_Air Sungai': 0,
        'sumber_air_minum_Lainnya': 0,
        'sumber_air_minum_Leding Eceran': 0,
        'sumber_air_minum_Leding Meteran': 0,
        'sumber_air_minum_Mata Air Tak Terlindung': 0,
        'sumber_air_minum_Mata Air Terlindung': 0,
        'sumber_air_minum_Sumur': 0,
        'sumber_air_minum_Sumur Bor': 0,
        'sumber_air_minum_Sumur Tak Terlindung': 0,
        'sumber_air_minum_Sumur Terlindung': 0,
        'cara_peroleh_air_minum_Langganan': 0,
        'cara_peroleh_air_minum_Membeli Eceran': 0,
        'cara_peroleh_air_minum_Tidak Membeli': 0,
        'sumber_penerangan_utama_Bukan Listrik': 0,
        'sumber_penerangan_utama_Listrik Non PLN': 0,
        'sumber_penerangan_utama_Listrik PLN': 0,
        'fasilitas_buang_air_besar_Bersama': 0,
        'fasilitas_buang_air_besar_Sendiri': 0,
        'fasilitas_buang_air_besar_Tidak Ada': 0,
        'fasilitas_buang_air_besar_Umum': 0,
        'buang_tinja_Kebun': 0,
        'buang_tinja_Kolam': 0,
        'buang_tinja_Lainnya': 0,
        'buang_tinja_Lubang Tanah': 0,
        'buang_tinja_SPAL': 0,
        'buang_tinja_Tangki' : 0,
    }
   data_result = { 
        'jumlah_anggota_rumah_tangga' : [request.form["jumlah_anggota_rumah_tangga"]],
        'jumlah_kamar' : [request.form["jumlah_kamar"]],
        'jumlah_sapi' : [request.form["jumlah_sapi"]],
        'jumlah_kerbau' : [request.form["jumlah_kerbau"]],
        'jumlah_kuda' : [request.form["jumlah_kuda"]],
        'jumlah_kambing' : [request.form["jumlah_kambing"]],
        'jumlah_babi' : [request.form["jumlah_babi"]],
        'status_kredit_usaha_rakyat' : [request.form["status_kredit_usaha_rakyat"]],
        'status_rastra' : [request.form["status_rastra"]],
        'status_jamsostek' : [request.form["status_jamsostek"]],
        'status_asuransi' : [request.form["status_asuransi"]],
        'status_bpjs_mandiri' : [request.form["status_bpjs_mandiri"]],
        'status_kis' : [request.form["status_kis"]],
        'status_kip' : [request.form["status_kip"]],
        'status_kks' : [request.form["status_kks"]],
        'status_usaha_art' : [request.form["status_usaha_art"]],
        'ada_kapal' : [request.form["ada_kapal"]],
        'ada_perahu' : [request.form["ada_perahu"]],
        'ada_mobil' : [request.form["ada_mobil"]],
        'ada_motor' : [request.form["ada_motor"]],
        'ada_sepeda' : [request.form["ada_sepeda"]],
        'ada_laptop' : [request.form["ada_laptop"]],
        'ada_emas' : [request.form["ada_emas"]],
        'ada_tv' : [request.form["ada_tv"]],
        'ada_telepon' : [request.form["ada_telepon"]],
        'ada_pemanas' : [request.form["ada_pemanas"]],
        'ada_ac' : [request.form["ada_ac"]],
        'ada_lemari_es' : [request.form["ada_lemari_es"]],
        'ada_tabung_gas' : [request.form["ada_tabung_gas"]],
        'kepemilikan_rumah' : [request.form["kepemilikan_rumah"]],
        'kepemilikan_lahan' : [request.form["kepemilikan_lahan"]],
        'jenis_lantai' : [request.form["jenis_lantai"]],
        'jenis_dinding' : [request.form["jenis_dinding"]],
        'jenis_atap' : [request.form["jenis_atap"]],
        'sumber_air_minum' : [request.form["sumber_air_minum"]],
        'cara_peroleh_air_minum' : [request.form["cara_peroleh_air_minum"]],
        'sumber_penerangan_utama' : [request.form["sumber_penerangan_utama"]],
        'fasilitas_buang_air_besar' : [request.form["fasilitas_buang_air_besar"]],
        'buang_tinja' : [request.form["buang_tinja"]],
    }
   if request.form["kepemilikan_rumah"] == '0':
    data['kepemilikan_rumah_Milik Sendiri'] = 1,
   elif request.form["kepemilikan_rumah"] == '1':
        data['kepemilikan_rumah_Bebas Sewa'] = 1, 
   elif request.form["kepemilikan_rumah"] == '2':
        data['kepemilikan_rumah_Kontrak'] = 1,    
   elif request.form["kepemilikan_rumah"] == '3':
        data['kepemilikan_rumah_Dinas'] = 1,
   else:
        data['kepemilikan_rumah_Lainnya'] = 1,


        # kepemilikan lahan
   if request.form['kepemilikan_lahan'] == '0':
            data['kepemilikan_lahan_Milik Sendiri'] = 1,
   elif request.form["kepemilikan_lahan"] == '1':
            data['kepemilikan_lahan_Milik Orang Lain'] = 1,
        
   elif request.form["kepemilikan_lahan"] == '2':
            data['kepemilikan_lahan_Tanah Negara'] = 1,
        
   else:
            data['kepemilikan_lahan_Lainnya'] = 1,

        # jenis lantai
   if request.form["jenis_lantai"] == '0':
            data['jenis_lantai_Marmer'] = 1,
        
   elif request.form["jenis_lantai"] == '1':
            data['jenis_lantai_Keramik'] = 1,
        
   elif request.form["jenis_lantai"] == '2':
            data['jenis_lantai_Parket'] = 1,
   elif request.form["jenis_lantai"] == '3':
            data['jenis_lantai_Ubin'] = 1,
        
   elif request.form["jenis_lantai"] == '4':
            data['jenis_lantai_Kayu'] = 1,
        
   elif request.form["jenis_lantai"] == '5':
            data['jenis_lantai_Bata Merah'] = 1,
        
   elif request.form["jenis_lantai"] == '6':
            data['jenis_lantai_Bambu'] = 1,
        
   elif request.form["jenis_lantai"] == '7':
            data['jenis_lantai_Tanah'] = 1,
        
   else:
            data['jenis_lantai_Lainnya'] = 1,

        # Jenis dinding
   if request.form["jenis_dinding"] == '0':
            data['jenis_dinding_Tembok'] = 1,
        
   elif request.form["jenis_dinding"] == '1':
            data['jenis_dinding_Plesteran'] = 1,
        
   elif request.form["jenis_dinding"] == '2':
            data['jenis_dinding_Kayu'] = 1,
        
   elif request.form["jenis_dinding"] == '3':
            data['jenis_dinding_Anyaman Bambu'] = 1,
        
   elif request.form["jenis_dinding"] == '4':
            data['jenis_dinding_Batang Kayu'] = 1,
        
   elif request.form["jenis_dinding"] == '5':
            data['jenis_dinding_Bambu'] = 1,
        
   else:
            data['jenis_dinding_Lainnya'] = 1,

        # jenis atap
   if request.form["jenis_atap"] == '0':
            data['jenis_atap_Seng'] = 1,
        
   elif request.form["jenis_atap"] == '1':
            data['jenis_atap_Beton'] = 1,
        
   elif request.form["jenis_atap"] == '2':
            data['jenis_atap_Genteng Keramik'] = 1,
        
   elif request.form["jenis_atap"] == '3':
            data['jenis_atap_Asbes'] = 1,
        
   elif request.form["jenis_atap"] == '4':
            data['jenis_atap_Sirap'] = 1,
        
   elif request.form["jenis_atap"] == '5':
            data['jenis_atap_Bambu'] = 1,
        
   else:
            data['jenis_atap_Lainnya'] = 1,

        # sumber air minum
   if request.form["sumber_air_minum"] == '0':
            data['sumber_air_minum_Air Kemasan Bermerk'] = 1,
        
   elif request.form["sumber_air_minum"] == '1':
            data['sumber_air_minum_Air Isi Ulang'] = 1,
        
   elif request.form["sumber_air_minum"] =='2':
            data['sumber_air_minum_Leding Meteran'] = 1,
        
   elif request.form["sumber_air_minum"] == '3':
            data['sumber_air_minum_Leding Eceran'] = 1,
        
   elif request.form["sumber_air_minum"] == '4':
            data['sumber_air_minum_Sumur Bor'] = 1,
        
   elif request.form["sumber_air_minum"] == '5':
            data['sumber_air_minum_Sumur'] = 1,
        
   elif request.form["sumber_air_minum"] == '6':
            data['sumber_air_minum_Sumur Terlindung'] = 1,
        
   elif request.form["sumber_air_minum"] == '7':
            data['sumber_air_minum_Sumur Tak Terlindung'] = 1,
        
   elif request.form["sumber_air_minum"] == '8':
            data['sumber_air_minum_Mata Air Terlindung'] = 1,
        
   elif request.form["sumber_air_minum"] == '9':
            data['sumber_air_minum_Mata Air Tak Terlindung'] = 1,
        
   elif request.form["sumber_air_minum"] == '10':
            data['sumber_air_minum_Air Sungai'] = 1,
        
   elif request.form["sumber_air_minum"] == '11':
            data['sumber_air_minum_Air Hujan'] = 1,
        
   else:
            data['sumber_air_minum_Lainnya'] = 1,

        # cara peroleh air minum
   if request.form["cara_peroleh_air_minum"] == '0':
            data['cara_peroleh_air_minum_Tidak Membeli'] = 1,
        
   elif request.form["cara_peroleh_air_minum"] == '1':
            data['cara_peroleh_air_minum_Langganan'] = 1,
        
   else:
            data['cara_peroleh_air_minum_Membeli Eceran'] = 1,
        
         # Sumber Penerangan Utama
   if request.form["sumber_penerangan_utama"] == '0':
            data['sumber_penerangan_utama_Bukan Listrik'] = 1,
        
   elif request.form["sumber_penerangan_utama"] == '1':
            data['sumber_penerangan_utama_Listrik PLN'] = 1,
        
   else:
            data['sumber_penerangan_utama_Listrik Non PLN'] = 1,

        # Fasilitas Buang Air Besar
   if request.form["fasilitas_buang_air_besar"] == '0':
            data['fasilitas_buang_air_besar_Sendiri'] = 1,
        
   elif request.form["fasilitas_buang_air_besar"] == '1':
            data['fasilitas_buang_air_besar_Bersama'] = 1,
        
   elif request.form["fasilitas_buang_air_besar"] =='2':
            data['fasilitas_buang_air_besar_Umum'] = 1,
        
   else:
            data['fasilitas_buang_air_besar_Tidak Ada'] = 1,
        
        # Buang Tinja
   if request.form["buang_tinja"] == '0':
            data['buang_tinja_Kolam'] = 1,
        
   elif request.form["buang_tinja"] == '1':
            data['buang_tinja_Lubang Tanah'] = 1,
        
   elif request.form["buang_tinja"] == '2':
            data['buang_tinja_SPAL'] = 1,
        
   elif request.form["buang_tinja"] == '3':
            data['buang_tinja_Tangki'] = 1,
        
   elif request.form["buang_tinja"] == '4':
            data['buang_tinja_Kebun'] = 1,
        
   else:
            data['buang_tinja_Lainnya'] = 1,

        # lemari es
   if request.form["ada_kapal"]=='1':
            data['ada_kapal_Tidak'] = 0
   else:
            data['ada_kapal_Tidak'] = 1

        # ada telepom
   if request.form['ada_perahu'] == '1':
            data['ada_perahu_Tidak'] = 0
   else:
            data['ada_perahu_Tidak'] = 1

        # ada labtop
   if request.form['ada_mobil'] == '1':
            data['ada_mobil_Tidak'] = 0
   else:
            data['ada_mobil_Tidak'] = 1

        # ada sepeda
   if request.form['ada_motor'] == '1':
            data['ada_motor_Tidak'] = 0
   else:
            data['ada_motor_Tidak'] = 1

        # ada motor
   if request.form['ada_sepeda'] == '1':
            data['ada_sepeda_Tidak'] = 0
   else:
            data['ada_sepeda_Tidak'] = 1

        # ada perahu
   if request.form['ada_laptop'] == '1':
            data['ada_laptop_Tidak'] = 0
   else:
            data['ada_laptop_Tidak'] = 1
        
        # status usaha art
   if request.form['ada_emas'] == '1':
            data['ada_emas_Tidak'] = 0
   else:
            data['ada_emas_Tidak'] = 1

        # status rastra
   if request.form['ada_tv'] == '1':
            data['ada_tv_Tidak'] = 0
   else:
            data['ada_tv_Tidak'] = 1

        # status_kredit_usaha_rakyat
   if request.form["ada_telepon"]=='1':
            data['ada_telepon_Tidak'] = 0
   else:
            data['ada_telepon_Tidak'] = 1

         # status rastra
   if request.form['ada_pemanas'] == '1':
            data['ada_pemanas_Tidak'] = 0
   else:
            data['ada_pemanas_Tidak'] = 1

        # status_kredit_usaha_rakyat
   if request.form["ada_ac"]=='1':
            data['ada_ac_Tidak'] = 0
   else:
            data['ada_ac_Tidak'] = 1
              # status rastra
   if request.form['ada_lemari_es'] == '1':
            data['ada_lemari_es_Tidak'] = 0
   else:
            data['ada_lemari_es_Tidak'] = 1

        # status_kredit_usaha_rakyat
   if request.form["ada_tabung_gas"]=='1':
            data['ada_tabung_gas_Tidak'] = 0
   else:
            data['ada_tabung_gas_Tidak'] = 1

         # status_kredit_usaha_rakyat
   if request.form["status_kredit_usaha_rakyat"]=='1':
            data['status_kredit_usaha_rakyat_Tidak'] = 0
   else:
            data['status_kredit_usaha_rakyat_Tidak'] = 1
              # status rastra
   if request.form['status_rastra'] == '1':
            data['status_rastra_Tidak'] = 0
   else:
            data['status_rastra_Tidak'] = 1

        # status_kredit_usaha_rakyat
   if request.form["status_jamsostek"]=='1':
            data['status_jamsostek_Tidak'] = 0
   else:
            data['status_jamsostek_Tidak'] = 1

          # status_kredit_usaha_rakyat
   if request.form["status_bpjs_mandiri"]=='1':
            data['status_bpjs_mandiri_Tidak'] = 0
   else:
            data['status_bpjs_mandiri_Tidak'] = 1
              # status rastra
   if request.form['status_kis'] == '1':
            data['status_kis_Tidak'] = 0
   else:
            data['status_kis_Tidak'] = 1

        # status_kredit_usaha_rakyat
   if request.form["status_kip"]=='1':
            data['status_kip_Tidak'] = 0
   else:
            data['status_kip_Tidak'] = 1

           # status_kredit_usaha_rakyat
   if request.form["status_kks"]=='1':
            data['status_kks_Tidak'] = 0
   else:
            data['status_kks_Tidak'] = 1
              # status rastra
   if request.form['status_usaha_art'] == '1':
            data['status_usaha_art_Tidak'] = 0
   else:
            data['status_usaha_art_Tidak'] = 1

        # print (data['ada_motor_Tidak'])
        
   new_data = pd.DataFrame(data)
        # for i in new_data:
        #     print(i)
        # print(new_data.iloc[0])
        # new_data = pd.get_dummies(new_data)
        # predicted_result = []
        # model = request.form["model_classifier"]

   predicted_result = svm_model.predict(new_data)
    
   return render_template('resultsvm.html', data = data_result, result = predicted_result, model = svm_model)


@app.route('/svmpsopredict', methods=['POST'])
def svmpsopredict():
   data = {
        'jumlah_anggota_rumah_tangga' : [request.form["jumlah_anggota_rumah_tangga"]],
        'jumlah_kamar' : [request.form["jumlah_kamar"]],
        'jumlah_sapi' : [request.form["jumlah_sapi"]],
        'jumlah_kerbau' : [request.form["jumlah_kerbau"]],
        'jumlah_kuda' : [request.form["jumlah_kuda"]],
        'jumlah_kambing' : [request.form["jumlah_kambing"]],
        'jumlah_babi' : [request.form["jumlah_babi"]],
        'kepemilikan_rumah_Bebas Sewa' : 0,
        'kepemilikan_rumah_Dinas' : 0,
        'kepemilikan_rumah_Kontrak' : 0,
        'kepemilikan_rumah_Lainnya' : 0,
        'kepemilikan_rumah_Milik Sendiri' : 0,
        'kepemilikan_lahan_Lainnya' : 0,
        'kepemilikan_lahan_Milik Orang Lain' : 0,
        'kepemilikan_lahan_Milik Sendiri' : 0,
        'kepemilikan_lahan_Tanah Negara' : 0,
        'jenis_atap_Asbes': 0,
        'jenis_atap_Bambu': 0,
        'jenis_atap_Beton': 0,
        'jenis_atap_Genteng Keramik': 0,
        'jenis_atap_Lainnya': 0,
        'jenis_atap_Seng': 0,
        'jenis_atap_Sirap': 0,
        'sumber_penerangan_utama_Bukan Listrik': 0,
        'sumber_penerangan_utama_Listrik Non PLN': 0,
        'sumber_penerangan_utama_Listrik PLN': 0,
        'fasilitas_buang_air_besar_Bersama': 0,
        'fasilitas_buang_air_besar_Sendiri': 0,
        'fasilitas_buang_air_besar_Tidak Ada': 0,
        'fasilitas_buang_air_besar_Umum': 0,
        'buang_tinja_Kebun': 0,
        'buang_tinja_Kolam': 0,
        'buang_tinja_Lainnya': 0,
        'buang_tinja_Lubang Tanah': 0,
        'buang_tinja_SPAL': 0,
        'buang_tinja_Tangki' : 0,
        'ada_tv_Tidak' : [request.form["ada_tv"]],
        'ada_tv_Ya' : [request.form["ada_tv"]],
        'ada_emas_Tidak' : [request.form["ada_emas"]],
        'ada_emas_Ya' : [request.form["ada_emas"]],
        'ada_mobil_Tidak' : [request.form["ada_mobil"]],
        'ada_mobil_Ya' : [request.form["ada_mobil"]],
        'status_kks_Tidak' : [request.form["status_kks"]],
        'status_kks_Ya' : [request.form["status_kks"]],
        'status_bpjs_mandiri_Tidak' : [request.form["status_bpjs_mandiri"]],
        'status_bpjs_mandiri_Ya' : [request.form["status_bpjs_mandiri"]],
        'status_jamsostek_Tidak' : [request.form["status_jamsostek"]],
        'status_jamsostek_Ya' : [request.form["status_jamsostek"]],
        'status_asuransi_Tidak' : [request.form["status_asuransi"]],
        'status_asuransi_Ya' : [request.form["status_asuransi"]],
        'status_rastra_Tidak' : [request.form["status_rastra"]],
        'status_rastra_Ya' : [request.form["status_rastra"]],
        'status_kredit_usaha_rakyat_Tidak' : [request.form["status_kredit_usaha_rakyat"]],
        'status_kredit_usaha_rakyat_Ya' : [request.form["status_kredit_usaha_rakyat"]],
    }
   data_result = { 
        'jumlah_anggota_rumah_tangga' : [request.form["jumlah_anggota_rumah_tangga"]],
        'jumlah_kamar' : [request.form["jumlah_kamar"]],
        'jumlah_sapi' : [request.form["jumlah_sapi"]],
        'jumlah_kerbau' : [request.form["jumlah_kerbau"]],
        'jumlah_kuda' : [request.form["jumlah_kuda"]],
        'jumlah_kambing' : [request.form["jumlah_kambing"]],
        'jumlah_babi' : [request.form["jumlah_babi"]],
        'status_kredit_usaha_rakyat' : [request.form["status_kredit_usaha_rakyat"]],
        'status_rastra' : [request.form["status_rastra"]],
        'status_jamsostek' : [request.form["status_jamsostek"]],
        'status_asuransi' : [request.form["status_asuransi"]],
        'status_bpjs_mandiri' : [request.form["status_bpjs_mandiri"]],
        'status_kks' : [request.form["status_kks"]],
        'ada_mobil' : [request.form["ada_mobil"]],
        'ada_emas' : [request.form["ada_emas"]],
        'ada_tv' : [request.form["ada_tv"]],
        'kepemilikan_rumah' : [request.form["kepemilikan_rumah"]],
        'kepemilikan_lahan' : [request.form["kepemilikan_lahan"]],
        'jenis_atap' : [request.form["jenis_atap"]],
        'sumber_penerangan_utama' : [request.form["sumber_penerangan_utama"]],
        'fasilitas_buang_air_besar' : [request.form["fasilitas_buang_air_besar"]],
        'buang_tinja' : [request.form["buang_tinja"]],
    }
   if request.form["kepemilikan_rumah"] == '0':
    data['kepemilikan_rumah_Milik Sendiri'] = 1,
   elif request.form["kepemilikan_rumah"] == '1':
        data['kepemilikan_rumah_Bebas Sewa'] = 1, 
   elif request.form["kepemilikan_rumah"] == '2':
        data['kepemilikan_rumah_Kontrak'] = 1,    
   elif request.form["kepemilikan_rumah"] == '3':
        data['kepemilikan_rumah_Dinas'] = 1,
   else:
        data['kepemilikan_rumah_Lainnya'] = 1,


        # kepemilikan lahan
   if request.form['kepemilikan_lahan'] == '0':
            data['kepemilikan_lahan_Milik Sendiri'] = 1,
   elif request.form["kepemilikan_lahan"] == '1':
            data['kepemilikan_lahan_Milik Orang Lain'] = 1,
        
   elif request.form["kepemilikan_lahan"] == '2':
            data['kepemilikan_lahan_Tanah Negara'] = 1,
        
   else:
            data['kepemilikan_lahan_Lainnya'] = 1,

        # jenis atap
   if request.form["jenis_atap"] == '0':
            data['jenis_atap_Seng'] = 1,
        
   elif request.form["jenis_atap"] == '1':
            data['jenis_atap_Beton'] = 1,
        
   elif request.form["jenis_atap"] == '2':
            data['jenis_atap_Genteng Keramik'] = 1,
        
   elif request.form["jenis_atap"] == '3':
            data['jenis_atap_Asbes'] = 1,
        
   elif request.form["jenis_atap"] == '4':
            data['jenis_atap_Sirap'] = 1,
        
   elif request.form["jenis_atap"] == '5':
            data['jenis_atap_Bambu'] = 1,
        
   else:
            data['jenis_atap_Lainnya'] = 1,
        
         # Sumber Penerangan Utama
   if request.form["sumber_penerangan_utama"] == '0':
            data['sumber_penerangan_utama_Bukan Listrik'] = 1,
        
   elif request.form["sumber_penerangan_utama"] == '1':
            data['sumber_penerangan_utama_Listrik PLN'] = 1,
        
   else:
            data['sumber_penerangan_utama_Listrik Non PLN'] = 1,

        # Fasilitas Buang Air Besar
   if request.form["fasilitas_buang_air_besar"] == '0':
            data['fasilitas_buang_air_besar_Sendiri'] = 1,
        
   elif request.form["fasilitas_buang_air_besar"] == '1':
            data['fasilitas_buang_air_besar_Bersama'] = 1,
        
   elif request.form["fasilitas_buang_air_besar"] =='2':
            data['fasilitas_buang_air_besar_Umum'] = 1,
        
   else:
            data['fasilitas_buang_air_besar_Tidak Ada'] = 1,
        
        # Buang Tinja
   if request.form["buang_tinja"] == '0':
            data['buang_tinja_Kolam'] = 1,
        
   elif request.form["buang_tinja"] == '1':
            data['buang_tinja_Lubang Tanah'] = 1,
        
   elif request.form["buang_tinja"] == '2':
            data['buang_tinja_SPAL'] = 1,
        
   elif request.form["buang_tinja"] == '3':
            data['buang_tinja_Tangki'] = 1,
        
   elif request.form["buang_tinja"] == '4':
            data['buang_tinja_Kebun'] = 1,
        
   else:
            data['buang_tinja_Lainnya'] = 1,

        # ada labtop
   if request.form['ada_mobil'] == '1':
            data['ada_mobil_Tidak'] = 0
   else:
            data['ada_mobil_Tidak'] = 1
        
        # status usaha art
   if request.form['ada_emas'] == '1':
            data['ada_emas_Tidak'] = 0
   else:
            data['ada_emas_Tidak'] = 1

        # status rastra
   if request.form['ada_tv'] == '1':
            data['ada_tv_Tidak'] = 0
   else:
            data['ada_tv_Tidak'] = 1

         # status_kredit_usaha_rakyat
   if request.form["status_kredit_usaha_rakyat"]=='1':
            data['status_kredit_usaha_rakyat_Tidak'] = 0
   else:
            data['status_kredit_usaha_rakyat_Tidak'] = 1
              # status rastra
   if request.form['status_rastra'] == '1':
            data['status_rastra_Tidak'] = 0
   else:
            data['status_rastra_Tidak'] = 1

        # status_kredit_usaha_rakyat
   if request.form["status_jamsostek"]=='1':
            data['status_jamsostek_Tidak'] = 0
   else:
            data['status_jamsostek_Tidak'] = 1

          # status_kredit_usaha_rakyat
   if request.form["status_bpjs_mandiri"]=='1':
            data['status_bpjs_mandiri_Tidak'] = 0
   else:
            data['status_bpjs_mandiri_Tidak'] = 1

           # status_kredit_usaha_rakyat
   if request.form["status_kks"]=='1':
            data['status_kks_Tidak'] = 0
   else:
            data['status_kks_Tidak'] = 1
              # status rastra
        
   new_data = pd.DataFrame(data)
        # for i in new_data:
        #     print(i)
        # print(new_data.iloc[0])
        # new_data = pd.get_dummies(new_data)
        # predicted_result = []
        # model = request.form["model_classifier"]

   predicted_result = svmpso_model.predict(new_data)
    
   return render_template('resultsvmpso.html', data = data_result, result = predicted_result, model = svmpso_model)


if __name__ == '__main__':
    app.run()





