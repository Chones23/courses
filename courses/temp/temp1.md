<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
<body>
<style>
</style>
</head>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<body>
	<div id="footer-html" class="visible-pdf">
    		{% if not no_letterhead and footer %}
    		<div class="letter-head-footer">
    		</div>
    		{% endif %}
    		<p class="text-center small page-number visible-pdf">
    			{{ _("Page {0} of {1}").format('<span class="page"></span>', '<span class="topage"></span>') }}
    		</p>
    	</div>
<div class="container" style="width:100%">
  <img src="https://i21.servimg.com/u/f21/11/81/93/00/sampul12.png" alt="Human Design" style="width:100%;">
  <div class="centered" style="text-align:center">{{doc.nama_lengkap}}</div></div>

<div class="page-break"></div>
<a href="https://servimg.com/view/11819300/1909" target="_blank" ><img src="https://i.servimg.com/u/f21/11/81/93/00/111.jpg" border="0" alt="DISCLAIMER" /></a>
<div class="page-break"></div>
<a href="https://servimg.com/view/11819300/1910" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/210.jpg" border="0" alt="ABOUT HUMAN DESIGN" /></a>
<div class="page-break"></div>
<a href="https://servimg.com/view/11819300/1911" target="_blank" ><img src="https://i.servimg.com/u/f21/11/81/93/00/310.jpg" border="0" alt="HUMAN DESIGN" /></a>
<div class="page-break"></div>
<a href="https://servimg.com/view/11819300/1912" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/410.jpg" border="0" alt="NEUTRINOS" /></a>
<div class="page-break"></div>
<a href="https://servimg.com/view/11819300/1913" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/510.jpg" border="0" alt="HUMAN DESIGN" /></a>
<div class="page-break"></div>
<a href="https://servimg.com/view/11819300/1914" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/610.jpg" border="0" alt="HUMAN DESIGN" /></a>
<div class="page-break"></div>
<a href="https://servimg.com/view/11819300/1916" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/710.jpg" border="0" alt="9 PUSAT ENERGI" /></a>
<div class="page-break"></div>
<a href="https://servimg.com/view/11819300/1917" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/810.jpg" border="0" alt="YOU ARE UNIQUE" /></a>
<div class="page-break"></div>
<a href="https://servimg.com/view/11819300/1915" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/910.jpg" border="0" alt="DIRI SEJATI" /></a>
<div class="page-break"></div>
<a href="https://servimg.com/view/11819300/1920" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/1010.jpg" border="0" alt="64 GATES" /></a>
<div class="page-break"></div>
<a href="https://servimg.com/view/11819300/1919" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/1110.jpg" border="0" alt="PLANET" /></a>
<div class="page-break"></div>
<a href="https://servimg.com/view/11819300/1918" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/1210.jpg" border="0" alt="EMPTY GATES" /></a>
<div class="page-break"></div>
<a href="https://servimg.com/view/11819300/1923" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/1310.jpg" border="0" alt="HUMAN DESIGN" /></a>
<div class="page-break"></div>
<a href="https://servimg.com/view/11819300/1922" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/1410.jpg" border="0" alt="HUMAN DESIGN" /></a>
<div class="page-break"></div>
<h1 style="text-align: left;">BIODATA:</h1>
<p style="text-align: left;">Nama Lengkap: {{doc.nama_lengkap or " "}}</p>
<p style="text-align: left;">Tanggal Lahir: {{ doc.get_formatted("tgl_lahir") or " " }}</p>
<p style="text-align: left;">Jam Lahir: {{doc.jam_lahir or " "}}</p>
<p style="text-align: left;">Tempat Lahir: {{doc.tempat_lahir or " "}}</p>
<p style="text-align: left;"><br /><br />Dan inilah Bagan atau Chart Human Design saya, keunikan saya:</p>
<p style="text-align: left;"><br /><br /></p>
<p style="text-align: left;">{{doc.hd_bodygraph or " "}}</p>
<p style="text-align: left;"><br /><br /><br /><br /></p>
<p style="text-align: left;"><strong>Type Human Design Saya:</strong> {{doc.hd_type or " "}}</p>
<p style="text-align: left;"><strong>Inner Authority saya:</strong> {{doc.hd_inner_authority or " "}}</p>
<p style="text-align: left;"><strong>Strategi saya dalam mengambil keputusan atau tindakan:</strong> {{doc.hd_strategy or " "}}</p>
<p style="text-align: left;"><strong>Not-self theme saya:</strong> {{doc.hd_mynotself or " "}}</p>
<p style="text-align: left;"><strong>Profile saya:</strong> {{doc.hd_profile or " "}}</p>
<p style="text-align: left;"><strong>Definition saya:</strong> {{doc.hd_definition or " "}}</p>
<p style="text-align: left;"><strong>Incarnation Cross saya:</strong> {{doc.hd_incarnation_cross or " "}}</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;"><br /><br /></p>
<div class="page-break" style="text-align: left;">&nbsp;</div>
<h2 style="text-align: left;"><strong>TIPE HUMAN DESIGN</strong></h2>
<p style="text-align: left;"><strong>Type Human Design Saya:</strong> {{doc.hd_type or " "}}</p>
<p style="text-align: left;"><br /><br />{{doc.type or " "}}</p>
<div class="page-break" style="text-align: left;">&nbsp;</div>
<h2 style="text-align: left;"><strong>INNER AUTHORITY</strong></h2>
<p style="text-align: left;"><br /><br />{{doc.inner_auth or " "}}</p>
<p style="text-align: left;"><br /><br /></p>
<p style="text-align: left;"><strong>Inner Authority saya:</strong> {{doc.hd_inner_authority or " "}}</p>
<p style="text-align: left;"><br /><br />{{doc.authority or " "}}</p>
<div class="page-break" style="text-align: left;">&nbsp;</div>
<h2 style="text-align: left;"><strong>STRATEGI PENGAMBILAN KEPUTUSAN</strong></h2>
<p style="text-align: left;"><br /><br /></p>
<p style="text-align: left;"><strong>Strategi saya dalam mengambil keputusan atau tindakan:</strong> {{doc.hd_strategy or " "}}</p>
<p style="text-align: left;"><br /><br />{{doc.strategi_hd_auto or " "}}</p>
<div class="page-break" style="text-align: left;">&nbsp;</div>
<h2 style="text-align: left;"><strong>NOT SELF THEME / TEMA BUKAN DIRI / TEMA EMOSI</strong></h2>
<p style="text-align: left;"><br /><br /></p>
<p style="text-align: left;"><br /><a href="https://servimg.com/view/11819300/1838" target="_blank"><img src="https://i.servimg.com/u/f21/11/81/93/00/limpa_13.jpg" alt="Not self theme" border="0" /></a></p>
<p style="text-align: left;"><br /><br /></p>
<p style="text-align: left;">Pusat energi yang terbuka (tidak berwarna) di Body Graph Anda adalah salah satu reseptor utama dari pengondisian &mdash; atau pengaruh luar yang masuk ke dalam tubuh fisik Anda. Reseptor ini memengaruhi proses pengambilan keputusan pikiran Anda dan menciptakan apa yang disebut sebagai not-self theme alias tema bukan-diri atau tema emosi. Tema bukan-diri atau tema emosi akan menuntun Anda untuk membuat keputusan berdasarkan strategi yang diturunkan dari pengondisian pengaruh luar dan bukan berasal diri sejati Anda.</p>
<p style="text-align: left;"><br /><br /></p>
<p style="text-align: left;">Apakah "Not-self theme" atau tema "bukan-diri saya" alias "tema emosi" menurut Human Design? Apakah itu hal yang buruk? Tidak. Apakah itu hal yang baik? Tidak. Not-self theme ya not-self theme saja. Bukan baik atau buruk. Not-self theme adalah sesuatu yang kita jalani, dimana kita hidup berdampingan. Itu adalah bagian dari kita. Istilah "Bukan-Diri" hanyalah sebuah istilah yang digunakan untuk menggambarkan bagian dari diri kita yang secara keliru diidentifikasikan oleh pikiran sebagai "aku", sebagai siapa aku. Beberapa orang salah menafsirkan istilah ini sebagai hal yang buruk. Mereka mungkin berkata, "oh itu bukan diri Anda" atau "oh itu bukan diri saya", yang berarti dia atau saya melakukan sesuatu yang buruk atau salah. Ketika kita mengambil moralitas dari istilah tersebut, bagaimanapun, itu hanya menyatakan fakta: "itu bukan saya" atau "itu bukan kamu".</p>
<p style="text-align: left;"><br />Pikiranlah yang salah mengidentifikasi dengan Bukan-Diri. Pikiran menjadikannya pribadi dan menilai itu buruk. Sebenarnya, Jati Diri dan Bukan-Diri bercampur sebagai kita, sebagai satu. Kita bisa dengan mudah mengatakan "definisi" (diri sejati) dan "non-definisi" (bukan diri). Pada kenyataannya, kedua bagian ini tidak dapat dipisahkan; Diri-Sejati adalah definisi dan non-definisi yang hidup berdampingan secara sehat. Mereka adalah satu, dan hanya dibahas sebagai bagian individu sehingga pikiran kita dapat mulai membedakan antara apa yang kita dan bukan.</p>
<p style="text-align: left;"><br />Satu-satunya alasan ada istilah untuk "Bukan-Diri" adalah agar kita dapat keluar sejenak dan melihatnya secara obyektif, untuk melihatnya secara mekanis, untuk melihatnya ada di sana. Apabila Anda menjalani "Not-self theme" Anda maka Anda sedang menjalani kehidupan yang bukan dirancang untuk Anda.</p>
<p style="text-align: left;"><br />Not-self theme adalah cara tubuh Anda memberi tahu Anda bahwa ada sesuatu yang tidak selaras dalam kehidupan Anda dan hal tersebut membutuhkan perhatian Anda.</p>
<p style="text-align: left;"><br /><br /></p>
<p style="text-align: left;"><strong>Not-self theme saya:</strong> {{doc.hd_mynotself or " "}}</p>
<p style="text-align: left;"><br /><br />{{doc.not_self_theme or " "}}</p>
<div class="page-break" style="text-align: left;">&nbsp;</div>
<h2 style="text-align: left;"><strong>PROFIL HUMAN DESIGN</strong></h2>
<p style="text-align: left;"><br /><br /></p>
<p style="text-align: left;"><strong>Profile saya:</strong> {{doc.hd_profile or " "}}</p>
<p style="text-align: left;"><br /><br />{{doc.profile or " "}}</p>
<div class="page-break" style="text-align: left;">&nbsp;</div>
<h2 style="text-align: left;"><strong>DEFINITION</strong></h2>
<p style="text-align: left;"><br /><br /></p>
<p style="text-align: left;"><strong>Definition saya:</strong> {{doc.hd_definition or " "}}</p>
<p style="text-align: left;"><br /><br />{{doc.definitions or " "}}</p>
<div class="page-break" style="text-align: left;">&nbsp;</div>
<h2 style="text-align: left;"><strong>INCARNATION CROSS</strong></h2>
<p style="text-align: left;"><br /><br /></p><br>
<p style="text-align: left;"><a href="https://servimg.com/view/11819300/1834" target="_blank" rel="noopener"><img src="https://i21.servimg.com/u/f21/11/81/93/00/incarn11.png" alt="Image hosted by servimg.com" border="0" /></a></p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">&nbsp;</p>
<br>
<p style="text-align: left;"><em>Incarnation Cross</em> yang dikombinasikan dengan Tipe dan Profil <em>Human Design</em>, pada akhirnya akan menentukan tujuan hidup kita secara umum di Bumi ini. Ada 192 <em>Incarnation Cross</em> dalam Sistem <em>Human Design</em>, masing-masing berasal dari kombinasi tema posisi Matahari dan Bumi kita. Keduanya membentuk seluruh pengalaman kita sebagai manusia.</p>
<p style="text-align: left;">&nbsp;</p>
<br>
<p style="text-align: left;"><em>Incarnation Cross</em> Anda adalah sesuatu yang perlahan akan muncul seiring waktu saat Anda hidup bersama dengan sifat individual Anda, dan berpuncak pada ekspresi penuh potensi Anda. Ini biasanya mulai dimainkan di sekitar oposisi Uranus, yaitu di usia 38-42, ketika Anda telah menanam fondasi yang kokoh dan memiliki arah yang jelas dalam hidup Anda. Itulah inti dari tujuan hidup Anda, yang dengannya Anda dapat meninggalkan jejak Anda di Dunia ini...</p>
<br>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">Ini adalah jalan (atau alur cerita) yang dirancang untuk Anda jalani selama hidup Anda. Ini bukanlah takdir yang tak terelakkan &mdash; Anda dapat memilih untuk TIDAK menjalani jalan itu. Tetapi sebagian besar waktu kita tidak bisa tidak mengungkapkan <em>Incarnation Cross</em> kita, setidaknya sebagian, karena biasanya <em>Incarnation Cross</em> akan datang secara alami kepada kita.</p>
<p style="text-align: left;">&nbsp;</p>
<br>
<p style="text-align: left;">Jika hidup kita diibaratkan layaknya sebuah drama teater, maka Tipe <em>Human Design</em> Anda adalah peran yang Anda mainkan dalam drama teater tersebut. Misalnya, peran sebagai "Kepala Pelayan" mungkin memiliki peran tertentu dalam sebuah drama. Peran Anda dalam kehidupan ini adalah Tipe <em>Human Design</em> Anda yaitu: Manifestor, Generator, Manifesting Generator, Projector, atau Reflector, yang berarti Anda ada di sini untuk memulai, bekerja, membimbing, atau berefleksi &mdash; bergantung pada Tipe <em>Human Design</em> Anda.</p>
<p style="text-align: left;">&nbsp;</p>
<br>
<p style="text-align: left;">Profil Anda adalah kepribadian atau karakter yang Anda bawa ke dalam peran Anda. Dalam contoh kasus peran sebagai "Kepala Pelayan" diatas, beberapa Kepala Pelayan lebih banyak diam, beberapa bersifat tegas, beberapa tidak kompeten (biasanya dalam komedi), beberapa lebih pintar dari majikan mereka, beberapa melindungi majikan mereka (seperti tokoh Alfred di film Batman), dll. Ada banyak cara untuk memainkan peran sebagai seorang "Kepala Pelayan".</p>
<p style="text-align: left;">&nbsp;</p>
<br>
<p style="text-align: left;"><em>Incarnation Cross</em> adalah alur cerita yang dimainkan oleh karakter dalam perannya. Jadi <em>Incarnation Cross</em> Anda dapat dianggap sebagai tujuan hidup Anda dalam ruang lingkup yang luas, lalu itu akan dibuat sedikit lebih spesifik oleh Tipe dan Profil <em>Human Design</em> Anda, dan selanjutnya disempurnakan oleh sisa energi di Gerbang (<em>Gates</em>) Anda.</p>
<p style="text-align: left;">&nbsp;</p>
<br>
<p style="text-align: left;">Dan inilah hasil pembacaan <em>Incarnation Cross Anda</em>:</p>
<p style="text-align: left;">&nbsp;</p>
<br>
<p style="text-align: left;"><strong>Incarnation Cross saya:</strong> {{doc.hd_incarnation_cross or " "}}</p>
<p style="text-align: left;">&nbsp;</p>
<br>
<p style="text-align: left;">{{doc.incarnation_cross or " "}}</p>
<div class="page-break" style="text-align: left;">&nbsp;</div>
<a href="https://servimg.com/view/11819300/1924" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/112.jpg" border="0" alt="9 TITIK PUSAT ENERGI MANUSIA" /></a>
<a href="https://servimg.com/view/11819300/1926" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/211.jpg" border="0" alt="9 ENERGY CENTER" /></a>
<a href="https://servimg.com/view/11819300/1925" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/311.jpg" border="0" alt="HEAD CENTER" /></a>
<a href="https://servimg.com/view/11819300/1927" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/411.jpg" border="0" alt="AJNA" /></a>
<a href="https://servimg.com/view/11819300/1929" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/511.jpg" border="0" alt="THROAT CENTER" /></a>
<a href="https://servimg.com/view/11819300/1928" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/611.jpg" border="0" alt="IDENTITY CENTER" /></a>
<a href="https://servimg.com/view/11819300/1931" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/711.jpg" border="0" alt="HEART CENTER" /></a>
<a href="https://servimg.com/view/11819300/1932" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/811.jpg" border="0" alt="SOLAR PLEXUS" /></a>
<a href="https://servimg.com/view/11819300/1930" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/911.jpg" border="0" alt="ROOT CENTER" /></a>
<a href="https://servimg.com/view/11819300/1933" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/1011.jpg" border="0" alt="SPLEEN CENTER" /></a>
<a href="https://servimg.com/view/11819300/1934" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/1111.jpg" border="0" alt="SACRAL CENTER" /></a>
<div class="page-break"></div>
<a href="https://servimg.com/view/11819300/1921" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/1510.jpg" border="0" alt="HASIL PEMBACAAN HUMAN DESIGN" /></a>
<p style="text-align:left;">
<p><br>
{% for row in doc.gates %}
 {% if row.gates == 1 %}
<br/>
   <td class="text-right"><strong><small>{{ row.get_formatted("read") }}</small></strong>
<div class="page-break" style="text-align: left;">&nbsp;</div>
 {% endif %}
{% endfor %}
<div class="page-break"></div>
<h2 style="text-align: left;">THE CHANNEL / KANAL ENERGI</h2>
<p style="text-align: left;"><br /><br /></p>
<p style="text-align: left;"><a href="https://servimg.com/view/11819300/1835" target="_blank" rel="noopener"><img src="https://i21.servimg.com/u/f21/11/81/93/00/limpa_10.jpg" alt="Image hosted by servimg.com" width="943" height="667" border="0" /></a></p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">Ketika dua buah gate yang aktif atau terdefinisi saling bertemu dan menyatukan dua buah Center (Pusat Energi) yang berbeda, maka itu akan membentuk sebuah Channel (Kanal/Saluran).</p>
<p style="text-align: left;"><br />Berikut adalah penjelasan masing-masing channel. HARAP PERIKSA CHANNEL AKTIF ANDA ADA DI NOMOR BERAPA SAJA, LALU SESUAIKAN DAN BACALAH HASIL PEMBACAAN NYA DIBAWAH INI.<br /><br /></p>
<hr />
<!--channel-->
{% for row in doc.channel %}
 {% if row.channel == 1 %}
   <br />
   <td class="text-right"><strong><small>{{ row.get_formatted("read") }}</small></strong>
   <div class="page-break" style="text-align: left;">&nbsp;</div>
 {% endif %}
{% endfor %}
<!--channel-->
<a href="https://servimg.com/view/11819300/1935" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/113.jpg" border="0" alt="CATATAN TENTANG HUMAN DESIGN" /></a>
<a href="https://servimg.com/view/11819300/1936" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/212.jpg" border="0" alt="CATATAN TENTANG HUMAN DESIGN" /></a>
<a href="https://servimg.com/view/11819300/1937" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/312.jpg" border="0" alt="CATATAN TENTANG HUMAN DESIGN" /></a>
<a href="https://servimg.com/view/11819300/1939" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/412.jpg" border="0" alt="CATATAN TENTANG HUMAN DESIGN" /></a>
<a href="https://servimg.com/view/11819300/1938" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/512.jpg" border="0" alt="CATATAN TENTANG HUMAN DESIGN" /></a>
<a href="https://servimg.com/view/11819300/1940" target="_blank" ><img  src="https://i21.servimg.com/u/f21/11/81/93/00/612.jpg" border="0" alt="CATATAN TENTANG HUMAN DESIGN" /></a>

<h1 style="text-align: left;">CATATAN:</h1>
<div class="page-break" style="text-align: left;">&nbsp;</div>
<h1 style="text-align: left;">CATATAN:</h1>
<div class="page-break" style="text-align: left;">&nbsp;</div>
<div class="container" style="text-align: left;">&nbsp;</div>
<div class="page-break"></div>
<div class="container" style="width:100%"><img style="width: 100%;" src="https://i.servimg.com/u/f21/11/81/93/00/sampul11.png" height="auto" width="800px" alt="Human Design Book" />
</div></div></div>


.container {
  position: relative;
  text-align: center;
  color:black;
  font-size:20px;
  font-family: Arial,sans-serif;
  font-weight:bold;
  color: black;
}

.centered {
position: absolute;
width:100%;
text-align: center;
top: 85%;

}

.main {
    text-align: left;
    font-size:12px;
    font-family: Arial,sans-serif;
    color: black;
}

.print-format {
  background: white;
  width: 210mm;
  height: 297mm;
  margin-left:15mm;
  margin-top:16mm;
  margin-right:17mm;
  margin-bottom:22mm;
}
