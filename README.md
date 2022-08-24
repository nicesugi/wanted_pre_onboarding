**코드 컨벤션**

- 변수 : 스네이크 케이스
- 함수 : 스네이크 케이스
- 클래스 : 파스칼 케이스

---

**Git commit**

- Add : 새로운 프로젝트, 앱, 파일 생성
- Feat : 기능 추가, 수정, 삭제
- Update : 코드 수정 및 삭제
- Fix : 버그 수정
- Style: 코드에 영향을 주지 않는 변경사항 
- Comment : 주석 관련
- Test : 테스크 코드
- Docs : 문서 생성, 수정, 삭제
- Rename : 파일 혹은 폴더명을 수정하거나 옮기는 작업만인 경우
- Remove : 파일을 삭제하는 작업만 수행한 경우

---

**요구사항**
<br>
1. 채용공고를 등록합니다.<br>
1-1. 저장을 하기위한 모델들을 생성<br>
1-2. 1번에서 생성한 모델을 바탕으로 serializer 생성<br>
1-3. views.py에서 데이터 저장을 위해 post 메소드사용. <br>
1-4. serializer를 통하여 데이터 저장 구현<br>
<img width="718" alt="스크린샷 2022-08-24 오후 5 48 51" src="https://user-images.githubusercontent.com/104303285/186377320-f32d290d-336c-4367-97fe-c36ce9c68cb1.png">
<br>

---

2.채용공고를 수정합니다.<br>
2-1. views.py에 put메소드 구현<br>
2-2. partial = true를 통해 하나의 필드도 수정이 되도록 구현<br>
<img width="718" alt="스크린샷 2022-08-24 오후 5 56 46" src="https://user-images.githubusercontent.com/104303285/186377372-6dd61b02-4351-418e-b6a2-9a600c4764a0.png">
<br>

---

3.채용공고를 삭제합니다.<br>
3-1. views.py에 delete 메소드 구현<br>
<img width="718" alt="스크린샷 2022-08-24 오후 5 57 37" src="https://user-images.githubusercontent.com/104303285/186377410-c7b6789f-f614-4683-9455-f8a7ca60900b.png">
<br>

---

4-1. 채용공고 목록을 가져옵니다.<br>
4-1-1. views.py에 get 메소드 구현<br>
<img width="718" alt="스크린샷 2022-08-24 오후 5 58 07" src="https://user-images.githubusercontent.com/104303285/186377461-56de28b1-89ca-45c8-add5-1ca313c3e298.png">
<br>

---

4-2. 채용공고 검색 기능 구현<br>
4-2-1. views.py에 검색기능을 담당하는 새로운 View 구현<br>
4-2-2. get 메소드를 통하여 기능 구현<br>
4-2-3. query_params를 통하여 검색할 단어 받아오기<br>
4-2-4. contains를 통하여 특정 단어를 포함한 query_set들 반환<br>
4-2-5. query_set들을 |(백슬래쉬)를 이용하여 5번의 query_set들을 병합<br>
<img width="718" alt="스크린샷 2022-08-24 오후 5 59 01" src="https://user-images.githubusercontent.com/104303285/186377691-9f8d914a-653f-445a-aa6b-08e9bd79da4d.png">
<br>

---

5. 채용 상세 페이지를 가져옵니다.<br>
5-1. views.py에 상세페이지를 담당하는 새로운 View 구현<br>
<img width="718" alt="스크린샷 2022-08-24 오후 5 59 17" src="https://user-images.githubusercontent.com/104303285/186377752-dad204b8-a39b-45fe-b155-a58c64d12596.png">




