"""노트북(공책) 프로그램 만들기
    상속 class 연습
    """

class Note(object) :
    def __init__(self, contents = None):     # 넘어오는게 없을 때 None으로.
        self.contents = contents

    def writeContent(self, contents):
        self.contents = contents

    def removeAll(self, contents):
        self.contents = ""

    def __str__(self):
        return self.contents                # contents 내용 그대로 출력

class NoteBook(object):
    def __init__(self, tittle):
        #변수 초기화
        self.tittle = tittle
        self.pageNumber = 1                 #저장되어 있는 페이지의 갯수
        self.notes = {}                     #page는 key로 note 객체는 value로 저장

    def add_note(self, note, page_num=0) : #노트와 페이지 번호가 필요. page_num은 note객체를 저장할 key
        if len(self.notes.keys()) < 301 :           #저장된 note 개수를 체크 - 300페이지까지 저장가능
            if page_num == 0 :
                self.notes[self.pageNumber] = note        #넘어온 노트 저장
                self.pageNumber += 1
                print("*노트를 NoteBook에 추가했습니다*")
            else:
                if page_num not in self.notes.keys() :
                    self.notes[page_num] = note     # 넘어온 key(page번호)에 note 저장
                    print("*노트를 NoteBook에 추가했습니다*")
                else :
                    print("*해당 페이지에는 이미 노트가 존재합니다*")
        else :
            print("*더이상 노트를 추가할 수 없습니다*")


    def remove_note(self, page_num) :              #key를 넘겨주고 그 딕셔너리를 삭제해주면 됨.
        if page_num in self.notes.keys():
            del self.notes[page_num]
            print(page_num, "에 노트가 삭제되었습니다")
        else :
            print(page_num, "에 노트가 존재하지 않습니다")

    def get_number_of_page(self, page) :
        if page in self.notes.keys():
            return self.notes[page]
        else :
            print(page,'p에 note가 존재하지 않습니다.')


#객체생성
good_sentence = """쉽게만 살아가도 재미있어 빙고! - 최고심 """
note_1 = Note(good_sentence)
print("적은 글 : ",good_sentence)

good_sentence = """하루에 3시간을 걸으면 7년 후에 지구를 한 바퀴 돌 수 있다. - 사무엘 존슨"""
note_2 = Note()
note_2.writeContent(good_sentence)
print("적은 글 : ",good_sentence)

good_sentence = """오랫동안 꿈을 그리는 사람은 마침내 그 꿈을 닮아간다."""
note_3 = Note(good_sentence)
print("적은 글 : ",good_sentence)

notebook = NoteBook("명언 노트")
notebook.add_note(note_1)
print(notebook.notes.keys())
print('저장된 페이지 수' , notebook.get_number_of_page())
notebook.add_note(note_2)
print(notebook.notes.keys())
print('저장된 페이지 수' , notebook.get_number_of_page(2))

notebook.add_note(note_3, 2)
print(notebook.notes.keys())
print('저장된 페이지 수' , notebook.get_number_of_page(3))

notebook.add_note(note_3, 10)
print('저장된 페이지 수' , notebook.get_number_of_page(3))
print(notebook.notes.keys())

good_sentence = """생각은 창조하는 힘이 있다. """
note_4 = Note(good_sentence)
notebook.add_note(note_4, 10)
print('저장된 페이지 수' , notebook.get_number_of_page(4))
print(notebook.notes.keys())

good_sentence = """우리는 스스로 선택하고 품어온 생각 그대로 자신을 만든다. """
note_5 = Note(good_sentence)
notebook.add_note(note_5 )
print(notebook.get_number_of_page(5))
print(notebook.notes.keys())


print(notebook.get_number_of_page(3))  #3번 페이지에 저장된 note 의 내용 출력


notebook.remove_note(2)
