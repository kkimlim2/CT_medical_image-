# CT_medical_image 데이터 셋 


https://www.kaggle.com/kmader/siim-medical-images?select=dicom_dir


<p style="text-align: right;" data-ke-size="size16">2021. 09. 24 일부터 시작</p>

<p style="text-align: right;" data-ke-size="size16">&nbsp;</p>
<h3 data-ke-size="size26">&nbsp;0. 프로젝트의 배경&nbsp;</h2>
<p data-ke-size="size16">&nbsp;</p>
<p data-ke-size="size16">&nbsp;이번에 kubig에서 개인 프로젝트를 진행하게 되었다. 나는 2주 안에 완결낼 수 있으면서, DICOM 파일을 다룰 수 있는 프로젝트를 하고 싶었다. 캐글에서 과거에 아래와 같은 대회가 열렸음을 찾았고, 이와 관련한 프로젝트를 진행하고자 한다.&nbsp; 

<h3 data-ke-size="size23">1. 프로젝트의 목적</h3>
<p data-ke-size="size16">&nbsp;</p>
<p data-ke-size="size16">&nbsp;<span style="background-color: #f6e199;"> 'CT 사진으로부터 CONTRAST 사용 여부 확인하기'&nbsp;</span></p>
<p data-ke-size="size16">&nbsp;</p>
<p data-ke-size="size16">&nbsp;</p>
<p data-ke-size="size16">* contrast란?&nbsp;</p>
<p data-ke-size="size16"><a href="http://amc.seoul.kr/asan/healthinfo/easymediterm/easyMediTermDetail.do?dictId=3650">http://amc.seoul.kr/asan/healthinfo/easymediterm/easyMediTermDetail.do?dictId=3650</a>&nbsp;</p>


<p data-ke-size="size16">&nbsp;</p>
<h3 data-ke-size="size23">2. 프로젝트 데이터 셋</h3>
<p data-ke-size="size16">&nbsp;</p>
<p data-ke-size="size16">&nbsp;다양한 연령대와 성별의 환자들 lung CT 사진 DICOM 형식으로 모아 놓은 데이터 셋이다.&nbsp;</p>
<blockquote data-ke-style="style3"><b>Data Citation&nbsp;</b><br /><br />Albertina, B., Watson, M., Holback, C., Jarosz, R., Kirk, S., Lee, Y., &hellip; Lemmerman, J. (2016). Radiology Data from The Cancer Genome Atlas Lung Adenocarcinoma [TCGA-LUAD] collection. The Cancer Imaging Archive. http://doi.org/10.7937/K9/TCIA.2016.JGNIHEP5</blockquote>
<p data-ke-size="size16">&nbsp;</p>
<h3 data-ke-size="size23">3. 프로젝트 액션플랜&nbsp;</h3>
<p data-ke-size="size16">&nbsp;</p>
<table style="border-collapse: collapse; width: 100%; height: 133px;" border="1" data-ke-align="alignLeft">
<tbody>
<tr style="height: 19px;">
<td style="width: 22.6356%; text-align: center; height: 19px;">일자</td>
<td style="width: 44.031%; text-align: center; height: 19px;">목표</td>
<td style="width: 33.3333%; text-align: center; height: 19px;">활동로그&nbsp;</td>
</tr>
<tr style="height: 19px;">
<td style="width: 22.6356%; height: 19px; text-align: center;">~9/24</td>
<td style="width: 44.031%; height: 19px; text-align: center;">데이터 셋 서버에 옮겨놓기&nbsp;</td>
<td style="width: 33.3333%; height: 19px; text-align: center;">-</td>
</tr>
<tr style="height: 19px;">
<td style="width: 22.6356%; height: 19px; text-align: center;">9/25~9/26</td>
<td style="width: 44.031%; height: 19px; text-align: center;">DICOM 파일 array로 전환 및 시각화&nbsp;</td>
<td style="width: 33.3333%; height: 19px; text-align: center;"><a href="https://hyelimkungkung.tistory.com/47?category=935193" target="_blank" rel="noopener"><br />https://hyelimkungkung.tistory.com/47?category=935193&nbsp;&nbsp;</a></td>
</tr>
<tr style="height: 19px;">
<td style="width: 22.6356%; height: 19px; text-align: center;">9/27~9/29</td>
<td style="width: 44.031%; height: 19px; text-align: center;">DataLoader 만들기&nbsp;</td>
<td style="width: 33.3333%; height: 19px; text-align: center;"><a href="https://hyelimkungkung.tistory.com/48" target="_blank" rel="noopener"><br />https://hyelimkungkung.tistory.com/48&nbsp;&nbsp;</a>&nbsp;</td>
</tr>
<tr style="height: 19px;">
<td style="width: 22.6356%; height: 19px; text-align: center;">9/30~10/3</td>
<td style="width: 44.031%; height: 19px; text-align: center;">모델 만들기&nbsp;</td>
<td style="width: 33.3333%; height: 19px; text-align: center;">&nbsp;</td>
</tr>
<tr style="height: 19px;">
<td style="width: 22.6356%; text-align: center; height: 19px;">10/4</td>
<td style="width: 44.031%; text-align: center; height: 19px;">성능 지표 계산하기&nbsp;</td>
<td style="width: 33.3333%; text-align: center; height: 19px;">&nbsp;</td>
</tr>
<tr style="height: 19px;">
<td style="width: 22.6356%; text-align: center; height: 19px;">10/5~10/6</td>
<td style="width: 44.031%; text-align: center; height: 19px;">결과 정리 및 시각화&nbsp;</td>
<td style="width: 33.3333%; text-align: center; height: 19px;">&nbsp;</td>
</tr>
</tbody>
</table>
<p data-ke-size="size16">&nbsp;</p>
