import pytest


@pytest.fixture
def dict_data():
    return {"date": "12.01.2021", "eadep_department_id": 78}


@pytest.fixture
def dict_data_result():
    return {'date': '12.01.2021', 'eadep_department_id': 78}


@pytest.fixture
def string_data():
    return '{"date": "12.01.2021", "eadep_department_id": 78}'


@pytest.fixture
def string_data_result():
    return {'date': '12.01.2021', 'eadep_department_id': 78}


@pytest.fixture
def json_data():
    return '''
        {
          "receiptDate": "2021-08-17T11:36:06+03:00",
          "appealDate": null,
          "registrationDate": "2021-08-17",
          "deadlineDate": null,
          "authors": [],
          "nomenclature": {},
          "questions": [],
          "answers": [],
          "files": [],
          "pages": [],
          "coveringLetters": [],
          "appealParticipants": [],
          "curators": [],
          "resolutionCurators": [],
          "employees": [],
          "addresseeActingEmployees": [],
          "appealObjects": [],
          "authorOfLegals": [],
          "toNumber": [],
          "referringDocuments": [],
          "options": {},
          "numberPages": "1+0+1",
          "numberSignatures": 1,
          "isAdministrativeUse": true,
          "documentKind": "INCOMING",
          "medoDocumentKind": null,
          "typeReceipt": {},
          "typeRepeat": {},
          "documentType": {},
          "number": "АМ-4-10314/21 ДСП",
          "subjects": [],
          "coauthors": [],
          "withOutMainFile": null,
          "numberWasGenerated": true,
          "autoIncremented": false,
          "reservedNumber": null,
          "reservedNomenclature": null
        }
    '''


@pytest.fixture
def json_result():
    return {'receipt_date': '2021-08-17T11:36:06+03:00', 'appeal_date': None, 'registration_date': '2021-08-17', 'deadline_date': None, 'authors': [], 'nomenclature': {}, 'questions': [], 'answers': [], 'files': [], 'pages': [], 'covering_letters': [], 'appeal_participants': [], 'curators': [], 'resolution_curators': [], 'employees': [], 'addressee_acting_employees': [], 'appeal_objects': [], 'author_of_legals': [], 'to_number': [], 'referring_documents': [], 'options': {}, 'number_pages': '1+0+1', 'number_signatures': 1, 'is_administrative_use': True, 'document_kind': 'INCOMING', 'medo_document_kind': None, 'type_receipt': {}, 'type_repeat': {}, 'document_type': {}, 'number': 'АМ-4-10314/21 ДСП', 'subjects': [], 'coauthors': [], 'with_out_main_file': None, 'number_was_generated': True, 'auto_incremented': False, 'reserved_number': None, 'reserved_nomenclature': None}


@pytest.fixture
def make_code_string_result():
    return '''@dataclass
class TestFormData(BaseModel):
    receipt_date: Optional[str] = None
    appeal_date: Optional[str] = None
    registration_date: Optional[str] = None
    deadline_date: Optional[str] = None
    authors: list = field(default_factory=lambda: [])
    nomenclature: dict = field(default_factory=lambda: {})
    questions: list = field(default_factory=lambda: [])
    answers: list = field(default_factory=lambda: [])
    files: list = field(default_factory=lambda: [])
    pages: list = field(default_factory=lambda: [])
    covering_letters: list = field(default_factory=lambda: [])
    appeal_participants: list = field(default_factory=lambda: [])
    curators: list = field(default_factory=lambda: [])
    resolution_curators: list = field(default_factory=lambda: [])
    employees: list = field(default_factory=lambda: [])
    addressee_acting_employees: list = field(default_factory=lambda: [])
    appeal_objects: list = field(default_factory=lambda: [])
    author_of_legals: list = field(default_factory=lambda: [])
    to_number: list = field(default_factory=lambda: [])
    referring_documents: list = field(default_factory=lambda: [])
    options: dict = field(default_factory=lambda: {})
    number_pages: Optional[str] = None
    number_signatures: Optional[int] = None
    is_administrative_use: Optional[bool] = None
    document_kind: Optional[str] = None
    medo_document_kind: Optional[str] = None
    type_receipt: dict = field(default_factory=lambda: {})
    type_repeat: dict = field(default_factory=lambda: {})
    document_type: dict = field(default_factory=lambda: {})
    number: Optional[str] = None
    subjects: list = field(default_factory=lambda: [])
    coauthors: list = field(default_factory=lambda: [])
    with_out_main_file: Optional[str] = None
    number_was_generated: Optional[bool] = None
    auto_incremented: Optional[bool] = None
    reserved_number: Optional[str] = None
    reserved_nomenclature: Optional[str] = None


class TestFormDataBuilde(BaseBuilder):
    def __init__(self):
        super().__init__()
        self._receipt_date: Optional[str] = None
        self._appeal_date: Optional[str] = None
        self._registration_date: Optional[str] = None
        self._deadline_date: Optional[str] = None
        self._authors: Optional[list] = []
        self._nomenclature: dict = field(default_factory=lambda: {})
        self._questions: Optional[list] = []
        self._answers: Optional[list] = []
        self._files: Optional[list] = []
        self._pages: Optional[list] = []
        self._covering_letters: Optional[list] = []
        self._appeal_participants: Optional[list] = []
        self._curators: Optional[list] = []
        self._resolution_curators: Optional[list] = []
        self._employees: Optional[list] = []
        self._addressee_acting_employees: Optional[list] = []
        self._appeal_objects: Optional[list] = []
        self._author_of_legals: Optional[list] = []
        self._to_number: Optional[list] = []
        self._referring_documents: Optional[list] = []
        self._options: dict = field(default_factory=lambda: {})
        self._number_pages: Optional[str] = None
        self._number_signatures: Optional[int] = None
        self._is_administrative_use: Optional[bool] = None
        self._document_kind: Optional[str] = None
        self._medo_document_kind: Optional[str] = None
        self._type_receipt: dict = field(default_factory=lambda: {})
        self._type_repeat: dict = field(default_factory=lambda: {})
        self._document_type: dict = field(default_factory=lambda: {})
        self._number: Optional[str] = None
        self._subjects: Optional[list] = []
        self._coauthors: Optional[list] = []
        self._with_out_main_file: Optional[str] = None
        self._number_was_generated: Optional[bool] = None
        self._auto_incremented: Optional[bool] = None
        self._reserved_number: Optional[str] = None
        self._reserved_nomenclature: Optional[str] = None

    def with_receipt_date(self, receipt_date):
        self._receipt_date = receipt_date
        return self

    def with_appeal_date(self, appeal_date):
        self._appeal_date = appeal_date
        return self

    def with_registration_date(self, registration_date):
        self._registration_date = registration_date
        return self

    def with_deadline_date(self, deadline_date):
        self._deadline_date = deadline_date
        return self

    def with_authors(self, authors):
        self._authors = authors
        return self

    def with_nomenclature(self, nomenclature):
        self._nomenclature = nomenclature
        return self

    def with_questions(self, questions):
        self._questions = questions
        return self

    def with_answers(self, answers):
        self._answers = answers
        return self

    def with_files(self, files):
        self._files = files
        return self

    def with_pages(self, pages):
        self._pages = pages
        return self

    def with_covering_letters(self, covering_letters):
        self._covering_letters = covering_letters
        return self

    def with_appeal_participants(self, appeal_participants):
        self._appeal_participants = appeal_participants
        return self

    def with_curators(self, curators):
        self._curators = curators
        return self

    def with_resolution_curators(self, resolution_curators):
        self._resolution_curators = resolution_curators
        return self

    def with_employees(self, employees):
        self._employees = employees
        return self

    def with_addressee_acting_employees(self, addressee_acting_employees):
        self._addressee_acting_employees = addressee_acting_employees
        return self

    def with_appeal_objects(self, appeal_objects):
        self._appeal_objects = appeal_objects
        return self

    def with_author_of_legals(self, author_of_legals):
        self._author_of_legals = author_of_legals
        return self

    def with_to_number(self, to_number):
        self._to_number = to_number
        return self

    def with_referring_documents(self, referring_documents):
        self._referring_documents = referring_documents
        return self

    def with_options(self, options):
        self._options = options
        return self

    def with_number_pages(self, number_pages):
        self._number_pages = number_pages
        return self

    def with_number_signatures(self, number_signatures):
        self._number_signatures = number_signatures
        return self

    def with_is_administrative_use(self, is_administrative_use):
        self._is_administrative_use = is_administrative_use
        return self

    def with_document_kind(self, document_kind):
        self._document_kind = document_kind
        return self

    def with_medo_document_kind(self, medo_document_kind):
        self._medo_document_kind = medo_document_kind
        return self

    def with_type_receipt(self, type_receipt):
        self._type_receipt = type_receipt
        return self

    def with_type_repeat(self, type_repeat):
        self._type_repeat = type_repeat
        return self

    def with_document_type(self, document_type):
        self._document_type = document_type
        return self

    def with_number(self, number):
        self._number = number
        return self

    def with_subjects(self, subjects):
        self._subjects = subjects
        return self

    def with_coauthors(self, coauthors):
        self._coauthors = coauthors
        return self

    def with_with_out_main_file(self, with_out_main_file):
        self._with_out_main_file = with_out_main_file
        return self

    def with_number_was_generated(self, number_was_generated):
        self._number_was_generated = number_was_generated
        return self

    def with_auto_incremented(self, auto_incremented):
        self._auto_incremented = auto_incremented
        return self

    def with_reserved_number(self, reserved_number):
        self._reserved_number = reserved_number
        return self

    def with_reserved_nomenclature(self, reserved_nomenclature):
        self._reserved_nomenclature = reserved_nomenclature
        return self

    def build(self):
        return TestFormData(
            receipt_date=self._receipt_date,
            appeal_date=self._appeal_date,
            registration_date=self._registration_date,
            deadline_date=self._deadline_date,
            authors=self._authors,
            nomenclature=self._nomenclature,
            questions=self._questions,
            answers=self._answers,
            files=self._files,
            pages=self._pages,
            covering_letters=self._covering_letters,
            appeal_participants=self._appeal_participants,
            curators=self._curators,
            resolution_curators=self._resolution_curators,
            employees=self._employees,
            addressee_acting_employees=self._addressee_acting_employees,
            appeal_objects=self._appeal_objects,
            author_of_legals=self._author_of_legals,
            to_number=self._to_number,
            referring_documents=self._referring_documents,
            options=self._options,
            number_pages=self._number_pages,
            number_signatures=self._number_signatures,
            is_administrative_use=self._is_administrative_use,
            document_kind=self._document_kind,
            medo_document_kind=self._medo_document_kind,
            type_receipt=self._type_receipt,
            type_repeat=self._type_repeat,
            document_type=self._document_type,
            number=self._number,
            subjects=self._subjects,
            coauthors=self._coauthors,
            with_out_main_file=self._with_out_main_file,
            number_was_generated=self._number_was_generated,
            auto_incremented=self._auto_incremented,
            reserved_number=self._reserved_number,
            reserved_nomenclature=self._reserved_nomenclature,
        ).asdict()'''


@pytest.fixture
def nested_json_data():
    return '''{
  "receiptDate": "2021-08-19T09:41:36+03:00",
  "appealDate": null,
  "registrationDate": "2021-08-19",
  "deadlineDate": null,
  "authors": [
    {
      "contragent": {
        "birthday": null,
        "address": {}
      }
    }
  ],
  "nomenclature": {
    "department": {
      "archivedDate": null,
      "employees": null,
      "id": 220266,
      "code": null,
      "creationDate": "2020-11-23T10:28:14.768729+03:00",
      "updateDate": "2021-07-26T12:57:24.195+03:00",
      "name": "Тестовый АМиПМ",
      "fullName": "Тестовый АМиПМ",
      "phone": null,
      "employee": null,
      "departmentType": {
        "id": 34,
        "name": "Организация"
      },
      "parentDepartment": {
        "id": 30,
        "code": null,
        "creationDate": "2019-04-30T16:30:00.073863+03:00",
        "updateDate": "2021-06-23T11:59:41.298+03:00",
        "name": "Правительство Москвы",
        "fullName": "Правительство Москвы",
        "departmentType": null,
        "codeOrg": "A_ROOT",
        "blocked": false,
        "oibId": "71477449-bc80-423b-90df-8467b6afef10",
        "inn": null,
        "legalForm": null,
        "phones": null
      },
      "codeOrg": null,
      "blocked": false,
      "oibId": "2f0d7258-2d45-4f39-b42c-87f93bc40e02",
      "medoCode": "Тестовый АМиПМ",
      "isMedoDepartment": null,
      "medoSchemaVersion": null,
      "phones": null,
      "emails": null,
      "addresses": null,
      "inn": null,
      "isChecked": false,
      "legalForm": null
    },
    "direction": "INOUTINSIDE",
    "id": 4993,
    "code": "a164c94d-a58c-40e5-970a-2ccfe249d1cb",
    "creationDate": "2021-01-22T21:10:40.810901+03:00",
    "index": "АМ-4",
    "description": null,
    "deleted": null,
    "template": "%ИНДЕКС-%НОМЕР/%ГОД/2-%ТЕКСТ",
    "currentValue": 10457,
    "archivedDate": null
  },
  "questions": [
    {
      "addressees": [],
      "signers": [],
      "minDueDate": null,
      "timeOfAgenda": null,
      "dateOfAgenda": null,
      "answers": [],
      "questions": [],
      "serialNumber": 1,
      "category": {
        "id": 93,
        "parentId": null,
        "name": "1",
        "value": "1",
        "archivedDate": null
      },
      "annotation": "ьлол",
      "typeRepeat": {
        "id": 1,
        "value": "Первичное",
        "archivedDate": null
      }
    }
  ],
  "answers": [],
  "files": [
    {
      "employee": {
        "fullName": "АвтоАдминистратор Роман Сидорович",
        "employees": [],
        "id": 776937,
        "code": null,
        "creationDate": "2020-11-23T11:00:00.773535+03:00",
        "updateDate": "2021-07-22T13:09:22.107+03:00",
        "parentEmployee": null,
        "position": null,
        "oibLogin": "AvtoadministratorRS",
        "lastName": "АвтоАдминистратор",
        "firstName": "Роман",
        "middleName": "Сидорович",
        "phone": null,
        "personPhotoId": null,
        "email": null,
        "status": "ENABLED",
        "department": {
          "id": 220266,
          "employees": null,
          "code": null,
          "creationDate": "2020-11-23T10:28:14.768729+03:00",
          "updateDate": "2021-07-26T12:57:24.195+03:00",
          "name": "Тестовый АМиПМ",
          "fullName": "Тестовый АМиПМ",
          "phone": null,
          "employee": null,
          "departmentType": {
            "id": 34,
            "name": "Организация"
          },
          "parentDepartment": {
            "id": 30,
            "code": null,
            "creationDate": "2019-04-30T16:30:00.073863+03:00",
            "updateDate": "2021-06-23T11:59:41.298+03:00",
            "name": "Правительство Москвы",
            "fullName": "Правительство Москвы",
            "departmentType": null,
            "codeOrg": "A_ROOT",
            "blocked": false,
            "oibId": "71477449-bc80-423b-90df-8467b6afef10",
            "inn": null,
            "legalForm": null,
            "phones": null
          },
          "codeOrg": null,
          "blocked": false,
          "oibId": "2f0d7258-2d45-4f39-b42c-87f93bc40e02",
          "archivedDate": null,
          "medoCode": "Тестовый АМиПМ",
          "isMedoDepartment": null,
          "medoSchemaVersion": null,
          "phones": null,
          "emails": null,
          "addresses": null,
          "inn": null,
          "isChecked": false,
          "legalForm": null
        },
        "employeeType": {
          "id": 19,
          "name": "сотрудники"
        },
        "fioGenitive": "АвтоАдминистратора Романа Сидоровича",
        "fioDative": "АвтоАдминистратору Роману Сидоровичу",
        "fioAccusative": "АвтоАдминистратора Романа Сидоровича",
        "permissions": [
          "ANSWER_VIEW",
          "APPEAL_CREATE",
          "EXECUTION_MARK_BLOCK_DOWNLOAD",
          "PRINT_WITHOUT_FOOTER_DOCUMENT",
          "PARMA_ACCESS",
          "BLANK_FORM_ADD",
          "HISTORY_APPEAL_CREATE",
          "OUT_APPEAL_CREATE",
          "ATTACHMENT_UPLOAD_AND_DELETE",
          "ADD_REASON_FOR_PRINT",
          "DEPARTMENT_RESOLUTION_CAN_SEE",
          "ALL_APPEAL_VIEW",
          "ALL_INDEX_VIEW",
          "DOCUMENT_TYPE_CHANGE",
          "REQUEST_BLOCK_DOWNLOAD",
          "FOREIGN_RESOLUTION_CAN_SEE",
          "DEPARTMENT_WHITE_LIST_CREATE",
          "OTHER_APPEAL_SOME_EDIT",
          "ANSWER_ORGANIZATION_VIEW",
          "RESOLUTION_CREATE",
          "APPEAL_EDIT",
          "DSP_CREATE",
          "OWN_INDEX_VIEW",
          "QUESTION_EXECUTION",
          "FOREIGN_APPEAL_VIEW",
          "INSTEAD_RESOLUTION_CREATE",
          "SHOW_PRINT_RESOLUTION",
          "APPROVAL_SHEET_BLOCK_DOWNLOAD",
          "FILTERS_ALL_DOCUMENTS",
          "OBJECT_CREATE",
          "INTERNAL_APPEAL_REGISTERING",
          "OUR_APPEAL_ALL_EDIT_OG",
          "WORK_DIRECTORY",
          "APPEAL_EXECUTE",
          "INSTRUCTION_ADMIN",
          "LINKED_APPEAL_VIEW",
          "SETTING_EXPEDITE_DOCUMENT_REVIEW",
          "CREATE_PROTOCOL",
          "SETTING_ACCESS_STATUS_PROJECT_RESOLUTION",
          "FOLDER_PUBLIC_CREATE",
          "OUR_APPEAL_All_EDIT",
          "DSP_EDIT",
          "REPORT_ORDER_CONTROL_MY_DEPARTMENT",
          "RESOLUTION_CREATE_FROM_NAME",
          "SHOW_PRINT_DOCUMENT",
          "APPEAL_SHARE",
          "INTERNAL_APPEAL_CREATE",
          "FILTERS_PUBLIC_FOLDER",
          "analytics.access.only",
          "HAND_SIGNATURE_SETTING",
          "REPORT_ORDER_CONTROL",
          "DOCUMENTS_BLOCK_DOWNLOAD",
          "OTHER_APPEAL_All_EDIT",
          "OUR_RESOLUTION_All_EDIT",
          "AGREEMENT_LIST_CREATE",
          "HISTORY_RESOLUTION_CREATE",
          "RESOLUTION_DELETE",
          "CONTROL_EDIT",
          "APPEAL_ARCHIVE",
          "DELETED_FOLDER_FOR_DOCUMENT",
          "FILTERS_EXECUTIONS",
          "OPERATIONAL_REPORT_ACCESS",
          "APPROVE_RESOLUTION_CAN_SEE",
          "MAILING_LIST_SETTING",
          "REDIRECTING_INCOMING_DOCUMENTS_WITHOUT_REGISTRATION",
          "ANSWER_ALL_QUESTIONS",
          "FILTERS_HAND_SIGNATURE",
          "REPORT_SENDING_DOCUMENTS_ALL_ORG",
          "DISCHARGE_OF_DUTIES_POSTPONE",
          "ORGANIZATION_HISTORY_VIEW",
          "MAINTAINING_DIRECTORY_DATA",
          "OUR_PROTOCOL_EDIT",
          "RESERVE_NUMBER",
          "FILTERS_REGISTERING",
          "OUTGOING_DOCUMENTS_BLOCK_DOWNLOAD",
          "CREATE_ITEM_PROTOCOL",
          "APPEAL_UNIT_DOCUMENTS_SHOW",
          "OTHER_ORGANIZATION_HISTORY_VIEW",
          "DISCHARGE_OF_DUTIES_REDISTRIBUTION",
          "DISCHARGE_OF_DUTIES_MANAGEMENT",
          "EXECUTION_MARK_CREATE_FROM_NAME",
          "FILTERS_APPROVEMENT",
          "BLANK_FORM_ADD_IND",
          "BLANK_FORM_ADD_ORG",
          "DOCUMENT_DELETE",
          "APPEAL_CREATE_OG",
          "VIEW_REPORTS_OF_DOC",
          "EXECUTION_MARK_CREATE_GROUP",
          "CANCEL_RESOLUTION_BY_PROTOCOL_ITEM"
        ],
        "roles": [
          "APPEAL_REGISTRAR_BOSS",
          "test_2020-06-05"
        ],
        "blocked": false,
        "systemSettings": null,
        "oibID": "d6c147e2-3094-464d-a7c5-62c63a79571e",
        "archivedDate": null,
        "countAssignedAppeal": null,
        "isAprf": false,
        "isAmpm": null,
        "isAccessResolutionSetting": null,
        "disabledByWhiteList": null,
        "isFiltersSwitcherAvailable": true,
        "isMayorAssistant": null,
        "isMayor": null,
        "enableRecognition": null,
        "enableOgSearch": null,
        "rank": "LEADERSHIP",
        "isHasLeader": null,
        "assistantIds": null
      },
      "pages": [
        {
          "pages": [],
          "archivedDate": null,
          "uploadDate": null,
          "recognizedJson": null,
          "id": 5694845,
          "numberPage": 1,
          "height": 1118,
          "width": 796,
          "storageFileId": "2b4feb7c-6a22-4983-a402-a51d5ccbd287",
          "stamps": []
        }
      ],
      "archivedDate": null,
      "uploadDate": "2021-08-19T09:42:33+03:00",
      "recognizedJson": null,
      "id": 5694844,
      "fileName": "0000.pdf",
      "filePath": null,
      "temporary": true,
      "fileSize": 434379,
      "extension": "pdf",
      "recognitionState": null,
      "recognitionId": null,
      "storageFileId": "2fc3aa32-bfe4-4e35-a5cc-1e44eede0b16",
      "dependence": null,
      "numberPage": null,
      "fileType": "MAIN",
      "sourceType": "USER",
      "mergedFiles": [],
      "recognitionIsRead": null,
      "pageCountable": true,
      "showEveryone": null,
      "pageCount": 1,
      "pagesMetaInformation": null,
      "stamps": [],
      "addedPages": null,
      "convertedToPng": true,
      "ocrId": "db790d59b59171f989afa08ae6390954",
      "height": null,
      "width": null,
      "isFailedToConvert": null,
      "prevFileType": null,
      "invisible": false
    }
  ],
  "pages": [],
  "coveringLetters": [],
  "appealParticipants": [],
  "curators": [],
  "resolutionCurators": [],
  "employees": [],
  "addresseeActingEmployees": [
    {
      "employee": {
        "fullName": "АвтоРуководительОИВ2 Владимир Петрович",
        "employees": [],
        "id": 776955,
        "code": null,
        "creationDate": "2020-11-23T11:40:01.010416+03:00",
        "updateDate": "2021-04-28T14:59:06.492+03:00",
        "parentEmployee": null,
        "position": null,
        "oibLogin": "AvtorukovoditeloivVP",
        "lastName": "АвтоРуководительОИВ2",
        "firstName": "Владимир",
        "middleName": "Петрович",
        "phone": null,
        "personPhotoId": null,
        "email": null,
        "status": "ENABLED",
        "department": {
          "id": 220268,
          "employees": null,
          "code": null,
          "creationDate": "2020-11-23T10:28:14.80199+03:00",
          "updateDate": "2021-08-06T17:03:45.945+03:00",
          "name": "Тестовый ДЖКХ",
          "fullName": "Тестовый ДЖКХ",
          "phone": null,
          "employee": {
            "id": 776948,
            "code": null,
            "creationDate": "2020-11-23T11:40:00.856176+03:00",
            "updateDate": "2021-07-12T16:11:18.601+03:00",
            "position": null,
            "lastName": "РуководительДЖКХ-тест",
            "firstName": null,
            "middleName": null,
            "phone": null,
            "email": null,
            "employeeType": null,
            "isAprf": false
          },
          "departmentType": {
            "id": 34,
            "name": "Организация"
          },
          "parentDepartment": {
            "id": 220266,
            "code": null,
            "creationDate": "2020-11-23T10:28:14.768729+03:00",
            "updateDate": "2021-07-26T12:57:24.195+03:00",
            "name": "Тестовый АМиПМ",
            "fullName": "Тестовый АМиПМ",
            "departmentType": null,
            "codeOrg": null,
            "blocked": false,
            "oibId": "2f0d7258-2d45-4f39-b42c-87f93bc40e02",
            "inn": null,
            "legalForm": null,
            "phones": null
          },
          "codeOrg": null,
          "blocked": false,
          "oibId": "2c59751b-27dd-491c-b5af-d80101f55225",
          "archivedDate": null,
          "medoCode": null,
          "isMedoDepartment": null,
          "medoSchemaVersion": null,
          "phones": null,
          "emails": null,
          "addresses": null,
          "inn": null,
          "isChecked": false,
          "legalForm": null
        },
        "employeeType": {
          "id": 19,
          "name": "сотрудники"
        },
        "fioGenitive": "АвтоРуководительОИВ2 Владимира Петровича",
        "fioDative": "АвтоРуководительОИВ2 Владимиру Петровичу",
        "fioAccusative": "АвтоРуководительОИВ2 Владимира Петровича",
        "permissions": null,
        "roles": null,
        "blocked": false,
        "systemSettings": null,
        "oibID": "e3eebe8c-c160-43b8-8699-a19c9557ddbb",
        "archivedDate": null,
        "countAssignedAppeal": null,
        "isAprf": false,
        "isAmpm": null,
        "isAccessResolutionSetting": null,
        "disabledByWhiteList": null,
        "isFiltersSwitcherAvailable": false,
        "isMayorAssistant": null,
        "isMayor": null,
        "enableRecognition": null,
        "enableOgSearch": null,
        "rank": "LEADERSHIP",
        "isHasLeader": null,
        "assistantIds": null
      },
      "whoGaveRightsType": "DISCHARGE_OF_DUTIES"
    }
  ],
  "appealObjects": [],
  "authorOfLegals": [],
  "toNumber": [],
  "referringDocuments": [],
  "options": {},
  "numberPages": "1+0+1",
  "numberSignatures": 1,
  "isAdministrativeUse": true,
  "documentKind": "INCOMING",
  "medoDocumentKind": null,
  "typeReceipt": {
    "id": 74,
    "name": "Электронный документ",
    "archivedDate": null
  },
  "typeRepeat": {
    "id": 1,
    "value": "Первичное",
    "archivedDate": null
  },
  "documentType": {
    "id": 86,
    "pid": null,
    "typeName": "Служебное письмо",
    "archivedDate": null
  },
  "number": "АМ-4-10458/21 ДСП",
  "subjects": [],
  "coauthors": [],
  "withOutMainFile": null,
  "numberWasGenerated": true,
  "autoIncremented": false,
  "reservedNumber": null,
  "reservedNomenclature": null
}'''


@pytest.fixture
def rename_fields_result():
    return {'receipt_date': '2021-08-19T09:41:36+03:00', 'appeal_date': None, 'registration_date': '2021-08-19', 'deadline_date': None, 'authors': [{'contragent': {'birthday': None, 'address': {}}}], 'nomenclature': {'department': {'archived_date': None, 'employees': None, 'id': 220266, 'code': None, 'creation_date': '2020-11-23T10:28:14.768729+03:00', 'update_date': '2021-07-26T12:57:24.195+03:00', 'name': 'Тестовый АМиПМ', 'full_name': 'Тестовый АМиПМ', 'phone': None, 'employee': None, 'department_type': {'id': 34, 'name': 'Организация'}, 'parent_department': {'id': 30, 'code': None, 'creation_date': '2019-04-30T16:30:00.073863+03:00', 'update_date': '2021-06-23T11:59:41.298+03:00', 'name': 'Правительство Москвы', 'full_name': 'Правительство Москвы', 'department_type': None, 'code_org': 'A_ROOT', 'blocked': False, 'oib_id': '71477449-bc80-423b-90df-8467b6afef10', 'inn': None, 'legal_form': None, 'phones': None}, 'code_org': None, 'blocked': False, 'oib_id': '2f0d7258-2d45-4f39-b42c-87f93bc40e02', 'medo_code': 'Тестовый АМиПМ', 'is_medo_department': None, 'medo_schema_version': None, 'phones': None, 'emails': None, 'addresses': None, 'inn': None, 'is_checked': False, 'legal_form': None}, 'direction': 'INOUTINSIDE', 'id': 4993, 'code': 'a164c94d-a58c-40e5-970a-2ccfe249d1cb', 'creation_date': '2021-01-22T21:10:40.810901+03:00', 'index': 'АМ-4', 'description': None, 'deleted': None, 'template': '%ИНДЕКС-%НОМЕР/%ГОД/2-%ТЕКСТ', 'current_value': 10457, 'archived_date': None}, 'questions': [{'addressees': [], 'signers': [], 'min_due_date': None, 'time_of_agenda': None, 'date_of_agenda': None, 'answers': [], 'questions': [], 'serial_number': 1, 'category': {'id': 93, 'parent_id': None, 'name': '1', 'value': '1', 'archived_date': None}, 'annotation': 'ьлол', 'type_repeat': {'id': 1, 'value': 'Первичное', 'archived_date': None}}], 'answers': [], 'files': [{'employee': {'full_name': 'АвтоАдминистратор Роман Сидорович', 'employees': [], 'id': 776937, 'code': None, 'creation_date': '2020-11-23T11:00:00.773535+03:00', 'update_date': '2021-07-22T13:09:22.107+03:00', 'parent_employee': None, 'position': None, 'oib_login': 'AvtoadministratorRS', 'last_name': 'АвтоАдминистратор', 'first_name': 'Роман', 'middle_name': 'Сидорович', 'phone': None, 'person_photo_id': None, 'email': None, 'status': 'ENABLED', 'department': {'id': 220266, 'employees': None, 'code': None, 'creation_date': '2020-11-23T10:28:14.768729+03:00', 'update_date': '2021-07-26T12:57:24.195+03:00', 'name': 'Тестовый АМиПМ', 'full_name': 'Тестовый АМиПМ', 'phone': None, 'employee': None, 'department_type': {'id': 34, 'name': 'Организация'}, 'parent_department': {'id': 30, 'code': None, 'creation_date': '2019-04-30T16:30:00.073863+03:00', 'update_date': '2021-06-23T11:59:41.298+03:00', 'name': 'Правительство Москвы', 'full_name': 'Правительство Москвы', 'department_type': None, 'code_org': 'A_ROOT', 'blocked': False, 'oib_id': '71477449-bc80-423b-90df-8467b6afef10', 'inn': None, 'legal_form': None, 'phones': None}, 'code_org': None, 'blocked': False, 'oib_id': '2f0d7258-2d45-4f39-b42c-87f93bc40e02', 'archived_date': None, 'medo_code': 'Тестовый АМиПМ', 'is_medo_department': None, 'medo_schema_version': None, 'phones': None, 'emails': None, 'addresses': None, 'inn': None, 'is_checked': False, 'legal_form': None}, 'employee_type': {'id': 19, 'name': 'сотрудники'}, 'fio_genitive': 'АвтоАдминистратора Романа Сидоровича', 'fio_dative': 'АвтоАдминистратору Роману Сидоровичу', 'fio_accusative': 'АвтоАдминистратора Романа Сидоровича', 'permissions': ['ANSWER_VIEW', 'APPEAL_CREATE', 'EXECUTION_MARK_BLOCK_DOWNLOAD', 'PRINT_WITHOUT_FOOTER_DOCUMENT', 'PARMA_ACCESS', 'BLANK_FORM_ADD', 'HISTORY_APPEAL_CREATE', 'OUT_APPEAL_CREATE', 'ATTACHMENT_UPLOAD_AND_DELETE', 'ADD_REASON_FOR_PRINT', 'DEPARTMENT_RESOLUTION_CAN_SEE', 'ALL_APPEAL_VIEW', 'ALL_INDEX_VIEW', 'DOCUMENT_TYPE_CHANGE', 'REQUEST_BLOCK_DOWNLOAD', 'FOREIGN_RESOLUTION_CAN_SEE', 'DEPARTMENT_WHITE_LIST_CREATE', 'OTHER_APPEAL_SOME_EDIT', 'ANSWER_ORGANIZATION_VIEW', 'RESOLUTION_CREATE', 'APPEAL_EDIT', 'DSP_CREATE', 'OWN_INDEX_VIEW', 'QUESTION_EXECUTION', 'FOREIGN_APPEAL_VIEW', 'INSTEAD_RESOLUTION_CREATE', 'SHOW_PRINT_RESOLUTION', 'APPROVAL_SHEET_BLOCK_DOWNLOAD', 'FILTERS_ALL_DOCUMENTS', 'OBJECT_CREATE', 'INTERNAL_APPEAL_REGISTERING', 'OUR_APPEAL_ALL_EDIT_OG', 'WORK_DIRECTORY', 'APPEAL_EXECUTE', 'INSTRUCTION_ADMIN', 'LINKED_APPEAL_VIEW', 'SETTING_EXPEDITE_DOCUMENT_REVIEW', 'CREATE_PROTOCOL', 'SETTING_ACCESS_STATUS_PROJECT_RESOLUTION', 'FOLDER_PUBLIC_CREATE', 'OUR_APPEAL_All_EDIT', 'DSP_EDIT', 'REPORT_ORDER_CONTROL_MY_DEPARTMENT', 'RESOLUTION_CREATE_FROM_NAME', 'SHOW_PRINT_DOCUMENT', 'APPEAL_SHARE', 'INTERNAL_APPEAL_CREATE', 'FILTERS_PUBLIC_FOLDER', 'analytics.access.only', 'HAND_SIGNATURE_SETTING', 'REPORT_ORDER_CONTROL', 'DOCUMENTS_BLOCK_DOWNLOAD', 'OTHER_APPEAL_All_EDIT', 'OUR_RESOLUTION_All_EDIT', 'AGREEMENT_LIST_CREATE', 'HISTORY_RESOLUTION_CREATE', 'RESOLUTION_DELETE', 'CONTROL_EDIT', 'APPEAL_ARCHIVE', 'DELETED_FOLDER_FOR_DOCUMENT', 'FILTERS_EXECUTIONS', 'OPERATIONAL_REPORT_ACCESS', 'APPROVE_RESOLUTION_CAN_SEE', 'MAILING_LIST_SETTING', 'REDIRECTING_INCOMING_DOCUMENTS_WITHOUT_REGISTRATION', 'ANSWER_ALL_QUESTIONS', 'FILTERS_HAND_SIGNATURE', 'REPORT_SENDING_DOCUMENTS_ALL_ORG', 'DISCHARGE_OF_DUTIES_POSTPONE', 'ORGANIZATION_HISTORY_VIEW', 'MAINTAINING_DIRECTORY_DATA', 'OUR_PROTOCOL_EDIT', 'RESERVE_NUMBER', 'FILTERS_REGISTERING', 'OUTGOING_DOCUMENTS_BLOCK_DOWNLOAD', 'CREATE_ITEM_PROTOCOL', 'APPEAL_UNIT_DOCUMENTS_SHOW', 'OTHER_ORGANIZATION_HISTORY_VIEW', 'DISCHARGE_OF_DUTIES_REDISTRIBUTION', 'DISCHARGE_OF_DUTIES_MANAGEMENT', 'EXECUTION_MARK_CREATE_FROM_NAME', 'FILTERS_APPROVEMENT', 'BLANK_FORM_ADD_IND', 'BLANK_FORM_ADD_ORG', 'DOCUMENT_DELETE', 'APPEAL_CREATE_OG', 'VIEW_REPORTS_OF_DOC', 'EXECUTION_MARK_CREATE_GROUP', 'CANCEL_RESOLUTION_BY_PROTOCOL_ITEM'], 'roles': ['APPEAL_REGISTRAR_BOSS', 'test_2020-06-05'], 'blocked': False, 'system_settings': None, 'oib_i_d': 'd6c147e2-3094-464d-a7c5-62c63a79571e', 'archived_date': None, 'count_assigned_appeal': None, 'is_aprf': False, 'is_ampm': None, 'is_access_resolution_setting': None, 'disabled_by_white_list': None, 'is_filters_switcher_available': True, 'is_mayor_assistant': None, 'is_mayor': None, 'enable_recognition': None, 'enable_og_search': None, 'rank': 'LEADERSHIP', 'is_has_leader': None, 'assistant_ids': None}, 'pages': [{'pages': [], 'archived_date': None, 'upload_date': None, 'recognized_json': None, 'id': 5694845, 'number_page': 1, 'height': 1118, 'width': 796, 'storage_file_id': '2b4feb7c-6a22-4983-a402-a51d5ccbd287', 'stamps': []}], 'archived_date': None, 'upload_date': '2021-08-19T09:42:33+03:00', 'recognized_json': None, 'id': 5694844, 'file_name': '0000.pdf', 'file_path': None, 'temporary': True, 'file_size': 434379, 'extension': 'pdf', 'recognition_state': None, 'recognition_id': None, 'storage_file_id': '2fc3aa32-bfe4-4e35-a5cc-1e44eede0b16', 'dependence': None, 'number_page': None, 'file_type': 'MAIN', 'source_type': 'USER', 'merged_files': [], 'recognition_is_read': None, 'page_countable': True, 'show_everyone': None, 'page_count': 1, 'pages_meta_information': None, 'stamps': [], 'added_pages': None, 'converted_to_png': True, 'ocr_id': 'db790d59b59171f989afa08ae6390954', 'height': None, 'width': None, 'is_failed_to_convert': None, 'prev_file_type': None, 'invisible': False}], 'pages': [], 'covering_letters': [], 'appeal_participants': [], 'curators': [], 'resolution_curators': [], 'employees': [], 'addressee_acting_employees': [{'employee': {'full_name': 'АвтоРуководительОИВ2 Владимир Петрович', 'employees': [], 'id': 776955, 'code': None, 'creation_date': '2020-11-23T11:40:01.010416+03:00', 'update_date': '2021-04-28T14:59:06.492+03:00', 'parent_employee': None, 'position': None, 'oib_login': 'AvtorukovoditeloivVP', 'last_name': 'АвтоРуководительОИВ2', 'first_name': 'Владимир', 'middle_name': 'Петрович', 'phone': None, 'person_photo_id': None, 'email': None, 'status': 'ENABLED', 'department': {'id': 220268, 'employees': None, 'code': None, 'creation_date': '2020-11-23T10:28:14.80199+03:00', 'update_date': '2021-08-06T17:03:45.945+03:00', 'name': 'Тестовый ДЖКХ', 'full_name': 'Тестовый ДЖКХ', 'phone': None, 'employee': {'id': 776948, 'code': None, 'creation_date': '2020-11-23T11:40:00.856176+03:00', 'update_date': '2021-07-12T16:11:18.601+03:00', 'position': None, 'last_name': 'РуководительДЖКХ-тест', 'first_name': None, 'middle_name': None, 'phone': None, 'email': None, 'employee_type': None, 'is_aprf': False}, 'department_type': {'id': 34, 'name': 'Организация'}, 'parent_department': {'id': 220266, 'code': None, 'creation_date': '2020-11-23T10:28:14.768729+03:00', 'update_date': '2021-07-26T12:57:24.195+03:00', 'name': 'Тестовый АМиПМ', 'full_name': 'Тестовый АМиПМ', 'department_type': None, 'code_org': None, 'blocked': False, 'oib_id': '2f0d7258-2d45-4f39-b42c-87f93bc40e02', 'inn': None, 'legal_form': None, 'phones': None}, 'code_org': None, 'blocked': False, 'oib_id': '2c59751b-27dd-491c-b5af-d80101f55225', 'archived_date': None, 'medo_code': None, 'is_medo_department': None, 'medo_schema_version': None, 'phones': None, 'emails': None, 'addresses': None, 'inn': None, 'is_checked': False, 'legal_form': None}, 'employee_type': {'id': 19, 'name': 'сотрудники'}, 'fio_genitive': 'АвтоРуководительОИВ2 Владимира Петровича', 'fio_dative': 'АвтоРуководительОИВ2 Владимиру Петровичу', 'fio_accusative': 'АвтоРуководительОИВ2 Владимира Петровича', 'permissions': None, 'roles': None, 'blocked': False, 'system_settings': None, 'oib_i_d': 'e3eebe8c-c160-43b8-8699-a19c9557ddbb', 'archived_date': None, 'count_assigned_appeal': None, 'is_aprf': False, 'is_ampm': None, 'is_access_resolution_setting': None, 'disabled_by_white_list': None, 'is_filters_switcher_available': False, 'is_mayor_assistant': None, 'is_mayor': None, 'enable_recognition': None, 'enable_og_search': None, 'rank': 'LEADERSHIP', 'is_has_leader': None, 'assistant_ids': None}, 'who_gave_rights_type': 'DISCHARGE_OF_DUTIES'}], 'appeal_objects': [], 'author_of_legals': [], 'to_number': [], 'referring_documents': [], 'options': {}, 'number_pages': '1+0+1', 'number_signatures': 1, 'is_administrative_use': True, 'document_kind': 'INCOMING', 'medo_document_kind': None, 'type_receipt': {'id': 74, 'name': 'Электронный документ', 'archived_date': None}, 'type_repeat': {'id': 1, 'value': 'Первичное', 'archived_date': None}, 'document_type': {'id': 86, 'pid': None, 'type_name': 'Служебное письмо', 'archived_date': None}, 'number': 'АМ-4-10458/21 ДСП', 'subjects': [], 'coauthors': [], 'with_out_main_file': None, 'number_was_generated': True, 'auto_incremented': False, 'reserved_number': None, 'reserved_nomenclature': None}


@pytest.fixture
def rename_fields_data():
    return {'receiptDate': '2021-08-19T09:41:36+03:00', 'appealDate': None, 'registrationDate': '2021-08-19', 'deadlineDate': None, 'authors': [{'contragent': {'birthday': None, 'address': {}}}], 'nomenclature': {'department': {'archivedDate': None, 'employees': None, 'id': 220266, 'code': None, 'creationDate': '2020-11-23T10:28:14.768729+03:00', 'updateDate': '2021-07-26T12:57:24.195+03:00', 'name': 'Тестовый АМиПМ', 'fullName': 'Тестовый АМиПМ', 'phone': None, 'employee': None, 'departmentType': {'id': 34, 'name': 'Организация'}, 'parentDepartment': {'id': 30, 'code': None, 'creationDate': '2019-04-30T16:30:00.073863+03:00', 'updateDate': '2021-06-23T11:59:41.298+03:00', 'name': 'Правительство Москвы', 'fullName': 'Правительство Москвы', 'departmentType': None, 'codeOrg': 'A_ROOT', 'blocked': False, 'oibId': '71477449-bc80-423b-90df-8467b6afef10', 'inn': None, 'legalForm': None, 'phones': None}, 'codeOrg': None, 'blocked': False, 'oibId': '2f0d7258-2d45-4f39-b42c-87f93bc40e02', 'medoCode': 'Тестовый АМиПМ', 'isMedoDepartment': None, 'medoSchemaVersion': None, 'phones': None, 'emails': None, 'addresses': None, 'inn': None, 'isChecked': False, 'legalForm': None}, 'direction': 'INOUTINSIDE', 'id': 4993, 'code': 'a164c94d-a58c-40e5-970a-2ccfe249d1cb', 'creationDate': '2021-01-22T21:10:40.810901+03:00', 'index': 'АМ-4', 'description': None, 'deleted': None, 'template': '%ИНДЕКС-%НОМЕР/%ГОД/2-%ТЕКСТ', 'currentValue': 10457, 'archivedDate': None}, 'questions': [{'addressees': [], 'signers': [], 'minDueDate': None, 'timeOfAgenda': None, 'dateOfAgenda': None, 'answers': [], 'questions': [], 'serialNumber': 1, 'category': {'id': 93, 'parentId': None, 'name': '1', 'value': '1', 'archivedDate': None}, 'annotation': 'ьлол', 'typeRepeat': {'id': 1, 'value': 'Первичное', 'archivedDate': None}}], 'answers': [], 'files': [{'employee': {'fullName': 'АвтоАдминистратор Роман Сидорович', 'employees': [], 'id': 776937, 'code': None, 'creationDate': '2020-11-23T11:00:00.773535+03:00', 'updateDate': '2021-07-22T13:09:22.107+03:00', 'parentEmployee': None, 'position': None, 'oibLogin': 'AvtoadministratorRS', 'lastName': 'АвтоАдминистратор', 'firstName': 'Роман', 'middleName': 'Сидорович', 'phone': None, 'personPhotoId': None, 'email': None, 'status': 'ENABLED', 'department': {'id': 220266, 'employees': None, 'code': None, 'creationDate': '2020-11-23T10:28:14.768729+03:00', 'updateDate': '2021-07-26T12:57:24.195+03:00', 'name': 'Тестовый АМиПМ', 'fullName': 'Тестовый АМиПМ', 'phone': None, 'employee': None, 'departmentType': {'id': 34, 'name': 'Организация'}, 'parentDepartment': {'id': 30, 'code': None, 'creationDate': '2019-04-30T16:30:00.073863+03:00', 'updateDate': '2021-06-23T11:59:41.298+03:00', 'name': 'Правительство Москвы', 'fullName': 'Правительство Москвы', 'departmentType': None, 'codeOrg': 'A_ROOT', 'blocked': False, 'oibId': '71477449-bc80-423b-90df-8467b6afef10', 'inn': None, 'legalForm': None, 'phones': None}, 'codeOrg': None, 'blocked': False, 'oibId': '2f0d7258-2d45-4f39-b42c-87f93bc40e02', 'archivedDate': None, 'medoCode': 'Тестовый АМиПМ', 'isMedoDepartment': None, 'medoSchemaVersion': None, 'phones': None, 'emails': None, 'addresses': None, 'inn': None, 'isChecked': False, 'legalForm': None}, 'employeeType': {'id': 19, 'name': 'сотрудники'}, 'fioGenitive': 'АвтоАдминистратора Романа Сидоровича', 'fioDative': 'АвтоАдминистратору Роману Сидоровичу', 'fioAccusative': 'АвтоАдминистратора Романа Сидоровича', 'permissions': ['ANSWER_VIEW', 'APPEAL_CREATE', 'EXECUTION_MARK_BLOCK_DOWNLOAD', 'PRINT_WITHOUT_FOOTER_DOCUMENT', 'PARMA_ACCESS', 'BLANK_FORM_ADD', 'HISTORY_APPEAL_CREATE', 'OUT_APPEAL_CREATE', 'ATTACHMENT_UPLOAD_AND_DELETE', 'ADD_REASON_FOR_PRINT', 'DEPARTMENT_RESOLUTION_CAN_SEE', 'ALL_APPEAL_VIEW', 'ALL_INDEX_VIEW', 'DOCUMENT_TYPE_CHANGE', 'REQUEST_BLOCK_DOWNLOAD', 'FOREIGN_RESOLUTION_CAN_SEE', 'DEPARTMENT_WHITE_LIST_CREATE', 'OTHER_APPEAL_SOME_EDIT', 'ANSWER_ORGANIZATION_VIEW', 'RESOLUTION_CREATE', 'APPEAL_EDIT', 'DSP_CREATE', 'OWN_INDEX_VIEW', 'QUESTION_EXECUTION', 'FOREIGN_APPEAL_VIEW', 'INSTEAD_RESOLUTION_CREATE', 'SHOW_PRINT_RESOLUTION', 'APPROVAL_SHEET_BLOCK_DOWNLOAD', 'FILTERS_ALL_DOCUMENTS', 'OBJECT_CREATE', 'INTERNAL_APPEAL_REGISTERING', 'OUR_APPEAL_ALL_EDIT_OG', 'WORK_DIRECTORY', 'APPEAL_EXECUTE', 'INSTRUCTION_ADMIN', 'LINKED_APPEAL_VIEW', 'SETTING_EXPEDITE_DOCUMENT_REVIEW', 'CREATE_PROTOCOL', 'SETTING_ACCESS_STATUS_PROJECT_RESOLUTION', 'FOLDER_PUBLIC_CREATE', 'OUR_APPEAL_All_EDIT', 'DSP_EDIT', 'REPORT_ORDER_CONTROL_MY_DEPARTMENT', 'RESOLUTION_CREATE_FROM_NAME', 'SHOW_PRINT_DOCUMENT', 'APPEAL_SHARE', 'INTERNAL_APPEAL_CREATE', 'FILTERS_PUBLIC_FOLDER', 'analytics.access.only', 'HAND_SIGNATURE_SETTING', 'REPORT_ORDER_CONTROL', 'DOCUMENTS_BLOCK_DOWNLOAD', 'OTHER_APPEAL_All_EDIT', 'OUR_RESOLUTION_All_EDIT', 'AGREEMENT_LIST_CREATE', 'HISTORY_RESOLUTION_CREATE', 'RESOLUTION_DELETE', 'CONTROL_EDIT', 'APPEAL_ARCHIVE', 'DELETED_FOLDER_FOR_DOCUMENT', 'FILTERS_EXECUTIONS', 'OPERATIONAL_REPORT_ACCESS', 'APPROVE_RESOLUTION_CAN_SEE', 'MAILING_LIST_SETTING', 'REDIRECTING_INCOMING_DOCUMENTS_WITHOUT_REGISTRATION', 'ANSWER_ALL_QUESTIONS', 'FILTERS_HAND_SIGNATURE', 'REPORT_SENDING_DOCUMENTS_ALL_ORG', 'DISCHARGE_OF_DUTIES_POSTPONE', 'ORGANIZATION_HISTORY_VIEW', 'MAINTAINING_DIRECTORY_DATA', 'OUR_PROTOCOL_EDIT', 'RESERVE_NUMBER', 'FILTERS_REGISTERING', 'OUTGOING_DOCUMENTS_BLOCK_DOWNLOAD', 'CREATE_ITEM_PROTOCOL', 'APPEAL_UNIT_DOCUMENTS_SHOW', 'OTHER_ORGANIZATION_HISTORY_VIEW', 'DISCHARGE_OF_DUTIES_REDISTRIBUTION', 'DISCHARGE_OF_DUTIES_MANAGEMENT', 'EXECUTION_MARK_CREATE_FROM_NAME', 'FILTERS_APPROVEMENT', 'BLANK_FORM_ADD_IND', 'BLANK_FORM_ADD_ORG', 'DOCUMENT_DELETE', 'APPEAL_CREATE_OG', 'VIEW_REPORTS_OF_DOC', 'EXECUTION_MARK_CREATE_GROUP', 'CANCEL_RESOLUTION_BY_PROTOCOL_ITEM'], 'roles': ['APPEAL_REGISTRAR_BOSS', 'test_2020-06-05'], 'blocked': False, 'systemSettings': None, 'oibID': 'd6c147e2-3094-464d-a7c5-62c63a79571e', 'archivedDate': None, 'countAssignedAppeal': None, 'isAprf': False, 'isAmpm': None, 'isAccessResolutionSetting': None, 'disabledByWhiteList': None, 'isFiltersSwitcherAvailable': True, 'isMayorAssistant': None, 'isMayor': None, 'enableRecognition': None, 'enableOgSearch': None, 'rank': 'LEADERSHIP', 'isHasLeader': None, 'assistantIds': None}, 'pages': [{'pages': [], 'archivedDate': None, 'uploadDate': None, 'recognizedJson': None, 'id': 5694845, 'numberPage': 1, 'height': 1118, 'width': 796, 'storageFileId': '2b4feb7c-6a22-4983-a402-a51d5ccbd287', 'stamps': []}], 'archivedDate': None, 'uploadDate': '2021-08-19T09:42:33+03:00', 'recognizedJson': None, 'id': 5694844, 'fileName': '0000.pdf', 'filePath': None, 'temporary': True, 'fileSize': 434379, 'extension': 'pdf', 'recognitionState': None, 'recognitionId': None, 'storageFileId': '2fc3aa32-bfe4-4e35-a5cc-1e44eede0b16', 'dependence': None, 'numberPage': None, 'fileType': 'MAIN', 'sourceType': 'USER', 'mergedFiles': [], 'recognitionIsRead': None, 'pageCountable': True, 'showEveryone': None, 'pageCount': 1, 'pagesMetaInformation': None, 'stamps': [], 'addedPages': None, 'convertedToPng': True, 'ocrId': 'db790d59b59171f989afa08ae6390954', 'height': None, 'width': None, 'isFailedToConvert': None, 'prevFileType': None, 'invisible': False}], 'pages': [], 'coveringLetters': [], 'appealParticipants': [], 'curators': [], 'resolutionCurators': [], 'employees': [], 'addresseeActingEmployees': [{'employee': {'fullName': 'АвтоРуководительОИВ2 Владимир Петрович', 'employees': [], 'id': 776955, 'code': None, 'creationDate': '2020-11-23T11:40:01.010416+03:00', 'updateDate': '2021-04-28T14:59:06.492+03:00', 'parentEmployee': None, 'position': None, 'oibLogin': 'AvtorukovoditeloivVP', 'lastName': 'АвтоРуководительОИВ2', 'firstName': 'Владимир', 'middleName': 'Петрович', 'phone': None, 'personPhotoId': None, 'email': None, 'status': 'ENABLED', 'department': {'id': 220268, 'employees': None, 'code': None, 'creationDate': '2020-11-23T10:28:14.80199+03:00', 'updateDate': '2021-08-06T17:03:45.945+03:00', 'name': 'Тестовый ДЖКХ', 'fullName': 'Тестовый ДЖКХ', 'phone': None, 'employee': {'id': 776948, 'code': None, 'creationDate': '2020-11-23T11:40:00.856176+03:00', 'updateDate': '2021-07-12T16:11:18.601+03:00', 'position': None, 'lastName': 'РуководительДЖКХ-тест', 'firstName': None, 'middleName': None, 'phone': None, 'email': None, 'employeeType': None, 'isAprf': False}, 'departmentType': {'id': 34, 'name': 'Организация'}, 'parentDepartment': {'id': 220266, 'code': None, 'creationDate': '2020-11-23T10:28:14.768729+03:00', 'updateDate': '2021-07-26T12:57:24.195+03:00', 'name': 'Тестовый АМиПМ', 'fullName': 'Тестовый АМиПМ', 'departmentType': None, 'codeOrg': None, 'blocked': False, 'oibId': '2f0d7258-2d45-4f39-b42c-87f93bc40e02', 'inn': None, 'legalForm': None, 'phones': None}, 'codeOrg': None, 'blocked': False, 'oibId': '2c59751b-27dd-491c-b5af-d80101f55225', 'archivedDate': None, 'medoCode': None, 'isMedoDepartment': None, 'medoSchemaVersion': None, 'phones': None, 'emails': None, 'addresses': None, 'inn': None, 'isChecked': False, 'legalForm': None}, 'employeeType': {'id': 19, 'name': 'сотрудники'}, 'fioGenitive': 'АвтоРуководительОИВ2 Владимира Петровича', 'fioDative': 'АвтоРуководительОИВ2 Владимиру Петровичу', 'fioAccusative': 'АвтоРуководительОИВ2 Владимира Петровича', 'permissions': None, 'roles': None, 'blocked': False, 'systemSettings': None, 'oibID': 'e3eebe8c-c160-43b8-8699-a19c9557ddbb', 'archivedDate': None, 'countAssignedAppeal': None, 'isAprf': False, 'isAmpm': None, 'isAccessResolutionSetting': None, 'disabledByWhiteList': None, 'isFiltersSwitcherAvailable': False, 'isMayorAssistant': None, 'isMayor': None, 'enableRecognition': None, 'enableOgSearch': None, 'rank': 'LEADERSHIP', 'isHasLeader': None, 'assistantIds': None}, 'whoGaveRightsType': 'DISCHARGE_OF_DUTIES'}], 'appealObjects': [], 'authorOfLegals': [], 'toNumber': [], 'referringDocuments': [], 'options': {}, 'numberPages': '1+0+1', 'numberSignatures': 1, 'isAdministrativeUse': True, 'documentKind': 'INCOMING', 'medoDocumentKind': None, 'typeReceipt': {'id': 74, 'name': 'Электронный документ', 'archivedDate': None}, 'typeRepeat': {'id': 1, 'value': 'Первичное', 'archivedDate': None}, 'documentType': {'id': 86, 'pid': None, 'typeName': 'Служебное письмо', 'archivedDate': None}, 'number': 'АМ-4-10458/21 ДСП', 'subjects': [], 'coauthors': [], 'withOutMainFile': None, 'numberWasGenerated': True, 'autoIncremented': False, 'reservedNumber': None, 'reservedNomenclature': None}


@pytest.fixture
def get_nested_dataclass_dict_result():
    return "{'receipt_date': '2021-08-19T09:41:36+03:00', 'appeal_date': None, 'registration_date': '2021-08-19', 'deadline_date': None, 'authors': [{'contragent': contragent(birthday=None, address=address())}], 'nomenclature': nomenclature(department=department(archived_date=None, employees=None, id=220266, code=None, creation_date='2020-11-23T10:28:14.768729+03:00', update_date='2021-07-26T12:57:24.195+03:00', name='Тестовый АМиПМ', full_name='Тестовый АМиПМ', phone=None, employee=None, department_type=departmentType(id=34, name='Организация'), parent_department=parentDepartment(id=30, code=None, creation_date='2019-04-30T16:30:00.073863+03:00', update_date='2021-06-23T11:59:41.298+03:00', name='Правительство Москвы', full_name='Правительство Москвы', department_type=None, code_org='A_ROOT', blocked=False, oib_id='71477449-bc80-423b-90df-8467b6afef10', inn=None, legal_form=None, phones=None), code_org=None, blocked=False, oib_id='2f0d7258-2d45-4f39-b42c-87f93bc40e02', medo_code='Тестовый АМиПМ', is_medo_department=None, medo_schema_version=None, phones=None, emails=None, addresses=None, inn=None, is_checked=False, legal_form=None), direction='INOUTINSIDE', id=4993, code='a164c94d-a58c-40e5-970a-2ccfe249d1cb', creation_date='2021-01-22T21:10:40.810901+03:00', index='АМ-4', description=None, deleted=None, template='%ИНДЕКС-%НОМЕР/%ГОД/2-%ТЕКСТ', current_value=10457, archived_date=None), 'questions': [{'addressees': [], 'signers': [], 'min_due_date': None, 'time_of_agenda': None, 'date_of_agenda': None, 'answers': [], 'questions': [], 'serial_number': 1, 'category': category(id=93, parent_id=None, name='1', value='1', archived_date=None), 'annotation': 'ьлол', 'type_repeat': typeRepeat(id=1, value='Первичное', archived_date=None)}], 'answers': [], 'files': [{'employee': employee(full_name='АвтоАдминистратор Роман Сидорович', employees=[], id=776937, code=None, creation_date='2020-11-23T11:00:00.773535+03:00', update_date='2021-07-22T13:09:22.107+03:00', parent_employee=None, position=None, oib_login='AvtoadministratorRS', last_name='АвтоАдминистратор', first_name='Роман', middle_name='Сидорович', phone=None, person_photo_id=None, email=None, status='ENABLED', department=department(id=220266, employees=None, code=None, creation_date='2020-11-23T10:28:14.768729+03:00', update_date='2021-07-26T12:57:24.195+03:00', name='Тестовый АМиПМ', full_name='Тестовый АМиПМ', phone=None, employee=None, department_type=departmentType(id=34, name='Организация'), parent_department=parentDepartment(id=30, code=None, creation_date='2019-04-30T16:30:00.073863+03:00', update_date='2021-06-23T11:59:41.298+03:00', name='Правительство Москвы', full_name='Правительство Москвы', department_type=None, code_org='A_ROOT', blocked=False, oib_id='71477449-bc80-423b-90df-8467b6afef10', inn=None, legal_form=None, phones=None), code_org=None, blocked=False, oib_id='2f0d7258-2d45-4f39-b42c-87f93bc40e02', archived_date=None, medo_code='Тестовый АМиПМ', is_medo_department=None, medo_schema_version=None, phones=None, emails=None, addresses=None, inn=None, is_checked=False, legal_form=None), employee_type=employeeType(id=19, name='сотрудники'), fio_genitive='АвтоАдминистратора Романа Сидоровича', fio_dative='АвтоАдминистратору Роману Сидоровичу', fio_accusative='АвтоАдминистратора Романа Сидоровича', permissions=['ANSWER_VIEW', 'APPEAL_CREATE', 'EXECUTION_MARK_BLOCK_DOWNLOAD', 'PRINT_WITHOUT_FOOTER_DOCUMENT', 'PARMA_ACCESS', 'BLANK_FORM_ADD', 'HISTORY_APPEAL_CREATE', 'OUT_APPEAL_CREATE', 'ATTACHMENT_UPLOAD_AND_DELETE', 'ADD_REASON_FOR_PRINT', 'DEPARTMENT_RESOLUTION_CAN_SEE', 'ALL_APPEAL_VIEW', 'ALL_INDEX_VIEW', 'DOCUMENT_TYPE_CHANGE', 'REQUEST_BLOCK_DOWNLOAD', 'FOREIGN_RESOLUTION_CAN_SEE', 'DEPARTMENT_WHITE_LIST_CREATE', 'OTHER_APPEAL_SOME_EDIT', 'ANSWER_ORGANIZATION_VIEW', 'RESOLUTION_CREATE', 'APPEAL_EDIT', 'DSP_CREATE', 'OWN_INDEX_VIEW', 'QUESTION_EXECUTION', 'FOREIGN_APPEAL_VIEW', 'INSTEAD_RESOLUTION_CREATE', 'SHOW_PRINT_RESOLUTION', 'APPROVAL_SHEET_BLOCK_DOWNLOAD', 'FILTERS_ALL_DOCUMENTS', 'OBJECT_CREATE', 'INTERNAL_APPEAL_REGISTERING', 'OUR_APPEAL_ALL_EDIT_OG', 'WORK_DIRECTORY', 'APPEAL_EXECUTE', 'INSTRUCTION_ADMIN', 'LINKED_APPEAL_VIEW', 'SETTING_EXPEDITE_DOCUMENT_REVIEW', 'CREATE_PROTOCOL', 'SETTING_ACCESS_STATUS_PROJECT_RESOLUTION', 'FOLDER_PUBLIC_CREATE', 'OUR_APPEAL_All_EDIT', 'DSP_EDIT', 'REPORT_ORDER_CONTROL_MY_DEPARTMENT', 'RESOLUTION_CREATE_FROM_NAME', 'SHOW_PRINT_DOCUMENT', 'APPEAL_SHARE', 'INTERNAL_APPEAL_CREATE', 'FILTERS_PUBLIC_FOLDER', 'analytics.access.only', 'HAND_SIGNATURE_SETTING', 'REPORT_ORDER_CONTROL', 'DOCUMENTS_BLOCK_DOWNLOAD', 'OTHER_APPEAL_All_EDIT', 'OUR_RESOLUTION_All_EDIT', 'AGREEMENT_LIST_CREATE', 'HISTORY_RESOLUTION_CREATE', 'RESOLUTION_DELETE', 'CONTROL_EDIT', 'APPEAL_ARCHIVE', 'DELETED_FOLDER_FOR_DOCUMENT', 'FILTERS_EXECUTIONS', 'OPERATIONAL_REPORT_ACCESS', 'APPROVE_RESOLUTION_CAN_SEE', 'MAILING_LIST_SETTING', 'REDIRECTING_INCOMING_DOCUMENTS_WITHOUT_REGISTRATION', 'ANSWER_ALL_QUESTIONS', 'FILTERS_HAND_SIGNATURE', 'REPORT_SENDING_DOCUMENTS_ALL_ORG', 'DISCHARGE_OF_DUTIES_POSTPONE', 'ORGANIZATION_HISTORY_VIEW', 'MAINTAINING_DIRECTORY_DATA', 'OUR_PROTOCOL_EDIT', 'RESERVE_NUMBER', 'FILTERS_REGISTERING', 'OUTGOING_DOCUMENTS_BLOCK_DOWNLOAD', 'CREATE_ITEM_PROTOCOL', 'APPEAL_UNIT_DOCUMENTS_SHOW', 'OTHER_ORGANIZATION_HISTORY_VIEW', 'DISCHARGE_OF_DUTIES_REDISTRIBUTION', 'DISCHARGE_OF_DUTIES_MANAGEMENT', 'EXECUTION_MARK_CREATE_FROM_NAME', 'FILTERS_APPROVEMENT', 'BLANK_FORM_ADD_IND', 'BLANK_FORM_ADD_ORG', 'DOCUMENT_DELETE', 'APPEAL_CREATE_OG', 'VIEW_REPORTS_OF_DOC', 'EXECUTION_MARK_CREATE_GROUP', 'CANCEL_RESOLUTION_BY_PROTOCOL_ITEM'], roles=['APPEAL_REGISTRAR_BOSS', 'test_2020-06-05'], blocked=False, system_settings=None, oib_i_d='d6c147e2-3094-464d-a7c5-62c63a79571e', archived_date=None, count_assigned_appeal=None, is_aprf=False, is_ampm=None, is_access_resolution_setting=None, disabled_by_white_list=None, is_filters_switcher_available=True, is_mayor_assistant=None, is_mayor=None, enable_recognition=None, enable_og_search=None, rank='LEADERSHIP', is_has_leader=None, assistant_ids=None), 'pages': [{'pages': [], 'archived_date': None, 'upload_date': None, 'recognized_json': None, 'id': 5694845, 'number_page': 1, 'height': 1118, 'width': 796, 'storage_file_id': '2b4feb7c-6a22-4983-a402-a51d5ccbd287', 'stamps': []}], 'archived_date': None, 'upload_date': '2021-08-19T09:42:33+03:00', 'recognized_json': None, 'id': 5694844, 'file_name': '0000.pdf', 'file_path': None, 'temporary': True, 'file_size': 434379, 'extension': 'pdf', 'recognition_state': None, 'recognition_id': None, 'storage_file_id': '2fc3aa32-bfe4-4e35-a5cc-1e44eede0b16', 'dependence': None, 'number_page': None, 'file_type': 'MAIN', 'source_type': 'USER', 'merged_files': [], 'recognition_is_read': None, 'page_countable': True, 'show_everyone': None, 'page_count': 1, 'pages_meta_information': None, 'stamps': [], 'added_pages': None, 'converted_to_png': True, 'ocr_id': 'db790d59b59171f989afa08ae6390954', 'height': None, 'width': None, 'is_failed_to_convert': None, 'prev_file_type': None, 'invisible': False}], 'pages': [], 'covering_letters': [], 'appeal_participants': [], 'curators': [], 'resolution_curators': [], 'employees': [], 'addressee_acting_employees': [{'employee': employee(full_name='АвтоРуководительОИВ2 Владимир Петрович', employees=[], id=776955, code=None, creation_date='2020-11-23T11:40:01.010416+03:00', update_date='2021-04-28T14:59:06.492+03:00', parent_employee=None, position=None, oib_login='AvtorukovoditeloivVP', last_name='АвтоРуководительОИВ2', first_name='Владимир', middle_name='Петрович', phone=None, person_photo_id=None, email=None, status='ENABLED', department=department(id=220268, employees=None, code=None, creation_date='2020-11-23T10:28:14.80199+03:00', update_date='2021-08-06T17:03:45.945+03:00', name='Тестовый ДЖКХ', full_name='Тестовый ДЖКХ', phone=None, employee=employee(id=776948, code=None, creation_date='2020-11-23T11:40:00.856176+03:00', update_date='2021-07-12T16:11:18.601+03:00', position=None, last_name='РуководительДЖКХ-тест', first_name=None, middle_name=None, phone=None, email=None, employee_type=None, is_aprf=False), department_type=departmentType(id=34, name='Организация'), parent_department=parentDepartment(id=220266, code=None, creation_date='2020-11-23T10:28:14.768729+03:00', update_date='2021-07-26T12:57:24.195+03:00', name='Тестовый АМиПМ', full_name='Тестовый АМиПМ', department_type=None, code_org=None, blocked=False, oib_id='2f0d7258-2d45-4f39-b42c-87f93bc40e02', inn=None, legal_form=None, phones=None), code_org=None, blocked=False, oib_id='2c59751b-27dd-491c-b5af-d80101f55225', archived_date=None, medo_code=None, is_medo_department=None, medo_schema_version=None, phones=None, emails=None, addresses=None, inn=None, is_checked=False, legal_form=None), employee_type=employeeType(id=19, name='сотрудники'), fio_genitive='АвтоРуководительОИВ2 Владимира Петровича', fio_dative='АвтоРуководительОИВ2 Владимиру Петровичу', fio_accusative='АвтоРуководительОИВ2 Владимира Петровича', permissions=None, roles=None, blocked=False, system_settings=None, oib_i_d='e3eebe8c-c160-43b8-8699-a19c9557ddbb', archived_date=None, count_assigned_appeal=None, is_aprf=False, is_ampm=None, is_access_resolution_setting=None, disabled_by_white_list=None, is_filters_switcher_available=False, is_mayor_assistant=None, is_mayor=None, enable_recognition=None, enable_og_search=None, rank='LEADERSHIP', is_has_leader=None, assistant_ids=None), 'who_gave_rights_type': 'DISCHARGE_OF_DUTIES'}], 'appeal_objects': [], 'author_of_legals': [], 'to_number': [], 'referring_documents': [], 'options': options(), 'number_pages': '1+0+1', 'number_signatures': 1, 'is_administrative_use': True, 'document_kind': 'INCOMING', 'medo_document_kind': None, 'type_receipt': typeReceipt(id=74, name='Электронный документ', archived_date=None), 'type_repeat': typeRepeat(id=1, value='Первичное', archived_date=None), 'document_type': documentType(id=86, pid=None, type_name='Служебное письмо', archived_date=None), 'number': 'АМ-4-10458/21 ДСП', 'subjects': [], 'coauthors': [], 'with_out_main_file': None, 'number_was_generated': True, 'auto_incremented': False, 'reserved_number': None, 'reserved_nomenclature': None}"


@pytest.fixture
def make_code_nested_dataclass_result():
    return 60849


@pytest.fixture
def make_code_nested_dataclass_data():
    return {'receipt_date': '2021-08-19T09:41:36+03:00', 'appeal_date': None, 'registration_date': '2021-08-19', 'deadline_date': None, 'authors': [{'contragent': {'birthday': None, 'address': {}}}], 'nomenclature': {'department': {'archived_date': None, 'employees': None, 'id': 220266, 'code': None, 'creation_date': '2020-11-23T10:28:14.768729+03:00', 'update_date': '2021-07-26T12:57:24.195+03:00', 'name': 'Тестовый АМиПМ', 'full_name': 'Тестовый АМиПМ', 'phone': None, 'employee': None, 'department_type': {'id': 34, 'name': 'Организация'}, 'parent_department': {'id': 30, 'code': None, 'creation_date': '2019-04-30T16:30:00.073863+03:00', 'update_date': '2021-06-23T11:59:41.298+03:00', 'name': 'Правительство Москвы', 'full_name': 'Правительство Москвы', 'department_type': None, 'code_org': 'A_ROOT', 'blocked': False, 'oib_id': '71477449-bc80-423b-90df-8467b6afef10', 'inn': None, 'legal_form': None, 'phones': None}, 'code_org': None, 'blocked': False, 'oib_id': '2f0d7258-2d45-4f39-b42c-87f93bc40e02', 'medo_code': 'Тестовый АМиПМ', 'is_medo_department': None, 'medo_schema_version': None, 'phones': None, 'emails': None, 'addresses': None, 'inn': None, 'is_checked': False, 'legal_form': None}, 'direction': 'INOUTINSIDE', 'id': 4993, 'code': 'a164c94d-a58c-40e5-970a-2ccfe249d1cb', 'creation_date': '2021-01-22T21:10:40.810901+03:00', 'index': 'АМ-4', 'description': None, 'deleted': None, 'template': '%ИНДЕКС-%НОМЕР/%ГОД/2-%ТЕКСТ', 'current_value': 10457, 'archived_date': None}, 'questions': [{'addressees': [], 'signers': [], 'min_due_date': None, 'time_of_agenda': None, 'date_of_agenda': None, 'answers': [], 'questions': [], 'serial_number': 1, 'category': {'id': 93, 'parent_id': None, 'name': '1', 'value': '1', 'archived_date': None}, 'annotation': 'ьлол', 'type_repeat': {'id': 1, 'value': 'Первичное', 'archived_date': None}}], 'answers': [], 'files': [{'employee': {'full_name': 'АвтоАдминистратор Роман Сидорович', 'employees': [], 'id': 776937, 'code': None, 'creation_date': '2020-11-23T11:00:00.773535+03:00', 'update_date': '2021-07-22T13:09:22.107+03:00', 'parent_employee': None, 'position': None, 'oib_login': 'AvtoadministratorRS', 'last_name': 'АвтоАдминистратор', 'first_name': 'Роман', 'middle_name': 'Сидорович', 'phone': None, 'person_photo_id': None, 'email': None, 'status': 'ENABLED', 'department': {'id': 220266, 'employees': None, 'code': None, 'creation_date': '2020-11-23T10:28:14.768729+03:00', 'update_date': '2021-07-26T12:57:24.195+03:00', 'name': 'Тестовый АМиПМ', 'full_name': 'Тестовый АМиПМ', 'phone': None, 'employee': None, 'department_type': {'id': 34, 'name': 'Организация'}, 'parent_department': {'id': 30, 'code': None, 'creation_date': '2019-04-30T16:30:00.073863+03:00', 'update_date': '2021-06-23T11:59:41.298+03:00', 'name': 'Правительство Москвы', 'full_name': 'Правительство Москвы', 'department_type': None, 'code_org': 'A_ROOT', 'blocked': False, 'oib_id': '71477449-bc80-423b-90df-8467b6afef10', 'inn': None, 'legal_form': None, 'phones': None}, 'code_org': None, 'blocked': False, 'oib_id': '2f0d7258-2d45-4f39-b42c-87f93bc40e02', 'archived_date': None, 'medo_code': 'Тестовый АМиПМ', 'is_medo_department': None, 'medo_schema_version': None, 'phones': None, 'emails': None, 'addresses': None, 'inn': None, 'is_checked': False, 'legal_form': None}, 'employee_type': {'id': 19, 'name': 'сотрудники'}, 'fio_genitive': 'АвтоАдминистратора Романа Сидоровича', 'fio_dative': 'АвтоАдминистратору Роману Сидоровичу', 'fio_accusative': 'АвтоАдминистратора Романа Сидоровича', 'permissions': ['ANSWER_VIEW', 'APPEAL_CREATE', 'EXECUTION_MARK_BLOCK_DOWNLOAD', 'PRINT_WITHOUT_FOOTER_DOCUMENT', 'PARMA_ACCESS', 'BLANK_FORM_ADD', 'HISTORY_APPEAL_CREATE', 'OUT_APPEAL_CREATE', 'ATTACHMENT_UPLOAD_AND_DELETE', 'ADD_REASON_FOR_PRINT', 'DEPARTMENT_RESOLUTION_CAN_SEE', 'ALL_APPEAL_VIEW', 'ALL_INDEX_VIEW', 'DOCUMENT_TYPE_CHANGE', 'REQUEST_BLOCK_DOWNLOAD', 'FOREIGN_RESOLUTION_CAN_SEE', 'DEPARTMENT_WHITE_LIST_CREATE', 'OTHER_APPEAL_SOME_EDIT', 'ANSWER_ORGANIZATION_VIEW', 'RESOLUTION_CREATE', 'APPEAL_EDIT', 'DSP_CREATE', 'OWN_INDEX_VIEW', 'QUESTION_EXECUTION', 'FOREIGN_APPEAL_VIEW', 'INSTEAD_RESOLUTION_CREATE', 'SHOW_PRINT_RESOLUTION', 'APPROVAL_SHEET_BLOCK_DOWNLOAD', 'FILTERS_ALL_DOCUMENTS', 'OBJECT_CREATE', 'INTERNAL_APPEAL_REGISTERING', 'OUR_APPEAL_ALL_EDIT_OG', 'WORK_DIRECTORY', 'APPEAL_EXECUTE', 'INSTRUCTION_ADMIN', 'LINKED_APPEAL_VIEW', 'SETTING_EXPEDITE_DOCUMENT_REVIEW', 'CREATE_PROTOCOL', 'SETTING_ACCESS_STATUS_PROJECT_RESOLUTION', 'FOLDER_PUBLIC_CREATE', 'OUR_APPEAL_All_EDIT', 'DSP_EDIT', 'REPORT_ORDER_CONTROL_MY_DEPARTMENT', 'RESOLUTION_CREATE_FROM_NAME', 'SHOW_PRINT_DOCUMENT', 'APPEAL_SHARE', 'INTERNAL_APPEAL_CREATE', 'FILTERS_PUBLIC_FOLDER', 'analytics.access.only', 'HAND_SIGNATURE_SETTING', 'REPORT_ORDER_CONTROL', 'DOCUMENTS_BLOCK_DOWNLOAD', 'OTHER_APPEAL_All_EDIT', 'OUR_RESOLUTION_All_EDIT', 'AGREEMENT_LIST_CREATE', 'HISTORY_RESOLUTION_CREATE', 'RESOLUTION_DELETE', 'CONTROL_EDIT', 'APPEAL_ARCHIVE', 'DELETED_FOLDER_FOR_DOCUMENT', 'FILTERS_EXECUTIONS', 'OPERATIONAL_REPORT_ACCESS', 'APPROVE_RESOLUTION_CAN_SEE', 'MAILING_LIST_SETTING', 'REDIRECTING_INCOMING_DOCUMENTS_WITHOUT_REGISTRATION', 'ANSWER_ALL_QUESTIONS', 'FILTERS_HAND_SIGNATURE', 'REPORT_SENDING_DOCUMENTS_ALL_ORG', 'DISCHARGE_OF_DUTIES_POSTPONE', 'ORGANIZATION_HISTORY_VIEW', 'MAINTAINING_DIRECTORY_DATA', 'OUR_PROTOCOL_EDIT', 'RESERVE_NUMBER', 'FILTERS_REGISTERING', 'OUTGOING_DOCUMENTS_BLOCK_DOWNLOAD', 'CREATE_ITEM_PROTOCOL', 'APPEAL_UNIT_DOCUMENTS_SHOW', 'OTHER_ORGANIZATION_HISTORY_VIEW', 'DISCHARGE_OF_DUTIES_REDISTRIBUTION', 'DISCHARGE_OF_DUTIES_MANAGEMENT', 'EXECUTION_MARK_CREATE_FROM_NAME', 'FILTERS_APPROVEMENT', 'BLANK_FORM_ADD_IND', 'BLANK_FORM_ADD_ORG', 'DOCUMENT_DELETE', 'APPEAL_CREATE_OG', 'VIEW_REPORTS_OF_DOC', 'EXECUTION_MARK_CREATE_GROUP', 'CANCEL_RESOLUTION_BY_PROTOCOL_ITEM'], 'roles': ['APPEAL_REGISTRAR_BOSS', 'test_2020-06-05'], 'blocked': False, 'system_settings': None, 'oib_i_d': 'd6c147e2-3094-464d-a7c5-62c63a79571e', 'archived_date': None, 'count_assigned_appeal': None, 'is_aprf': False, 'is_ampm': None, 'is_access_resolution_setting': None, 'disabled_by_white_list': None, 'is_filters_switcher_available': True, 'is_mayor_assistant': None, 'is_mayor': None, 'enable_recognition': None, 'enable_og_search': None, 'rank': 'LEADERSHIP', 'is_has_leader': None, 'assistant_ids': None}, 'pages': [{'pages': [], 'archived_date': None, 'upload_date': None, 'recognized_json': None, 'id': 5694845, 'number_page': 1, 'height': 1118, 'width': 796, 'storage_file_id': '2b4feb7c-6a22-4983-a402-a51d5ccbd287', 'stamps': []}], 'archived_date': None, 'upload_date': '2021-08-19T09:42:33+03:00', 'recognized_json': None, 'id': 5694844, 'file_name': '0000.pdf', 'file_path': None, 'temporary': True, 'file_size': 434379, 'extension': 'pdf', 'recognition_state': None, 'recognition_id': None, 'storage_file_id': '2fc3aa32-bfe4-4e35-a5cc-1e44eede0b16', 'dependence': None, 'number_page': None, 'file_type': 'MAIN', 'source_type': 'USER', 'merged_files': [], 'recognition_is_read': None, 'page_countable': True, 'show_everyone': None, 'page_count': 1, 'pages_meta_information': None, 'stamps': [], 'added_pages': None, 'converted_to_png': True, 'ocr_id': 'db790d59b59171f989afa08ae6390954', 'height': None, 'width': None, 'is_failed_to_convert': None, 'prev_file_type': None, 'invisible': False}], 'pages': [], 'covering_letters': [], 'appeal_participants': [], 'curators': [], 'resolution_curators': [], 'employees': [], 'addressee_acting_employees': [{'employee': {'full_name': 'АвтоРуководительОИВ2 Владимир Петрович', 'employees': [], 'id': 776955, 'code': None, 'creation_date': '2020-11-23T11:40:01.010416+03:00', 'update_date': '2021-04-28T14:59:06.492+03:00', 'parent_employee': None, 'position': None, 'oib_login': 'AvtorukovoditeloivVP', 'last_name': 'АвтоРуководительОИВ2', 'first_name': 'Владимир', 'middle_name': 'Петрович', 'phone': None, 'person_photo_id': None, 'email': None, 'status': 'ENABLED', 'department': {'id': 220268, 'employees': None, 'code': None, 'creation_date': '2020-11-23T10:28:14.80199+03:00', 'update_date': '2021-08-06T17:03:45.945+03:00', 'name': 'Тестовый ДЖКХ', 'full_name': 'Тестовый ДЖКХ', 'phone': None, 'employee': {'id': 776948, 'code': None, 'creation_date': '2020-11-23T11:40:00.856176+03:00', 'update_date': '2021-07-12T16:11:18.601+03:00', 'position': None, 'last_name': 'РуководительДЖКХ-тест', 'first_name': None, 'middle_name': None, 'phone': None, 'email': None, 'employee_type': None, 'is_aprf': False}, 'department_type': {'id': 34, 'name': 'Организация'}, 'parent_department': {'id': 220266, 'code': None, 'creation_date': '2020-11-23T10:28:14.768729+03:00', 'update_date': '2021-07-26T12:57:24.195+03:00', 'name': 'Тестовый АМиПМ', 'full_name': 'Тестовый АМиПМ', 'department_type': None, 'code_org': None, 'blocked': False, 'oib_id': '2f0d7258-2d45-4f39-b42c-87f93bc40e02', 'inn': None, 'legal_form': None, 'phones': None}, 'code_org': None, 'blocked': False, 'oib_id': '2c59751b-27dd-491c-b5af-d80101f55225', 'archived_date': None, 'medo_code': None, 'is_medo_department': None, 'medo_schema_version': None, 'phones': None, 'emails': None, 'addresses': None, 'inn': None, 'is_checked': False, 'legal_form': None}, 'employee_type': {'id': 19, 'name': 'сотрудники'}, 'fio_genitive': 'АвтоРуководительОИВ2 Владимира Петровича', 'fio_dative': 'АвтоРуководительОИВ2 Владимиру Петровичу', 'fio_accusative': 'АвтоРуководительОИВ2 Владимира Петровича', 'permissions': None, 'roles': None, 'blocked': False, 'system_settings': None, 'oib_i_d': 'e3eebe8c-c160-43b8-8699-a19c9557ddbb', 'archived_date': None, 'count_assigned_appeal': None, 'is_aprf': False, 'is_ampm': None, 'is_access_resolution_setting': None, 'disabled_by_white_list': None, 'is_filters_switcher_available': False, 'is_mayor_assistant': None, 'is_mayor': None, 'enable_recognition': None, 'enable_og_search': None, 'rank': 'LEADERSHIP', 'is_has_leader': None, 'assistant_ids': None}, 'who_gave_rights_type': 'DISCHARGE_OF_DUTIES'}], 'appeal_objects': [], 'author_of_legals': [], 'to_number': [], 'referring_documents': [], 'options': {}, 'number_pages': '1+0+1', 'number_signatures': 1, 'is_administrative_use': True, 'document_kind': 'INCOMING', 'medo_document_kind': None, 'type_receipt': {'id': 74, 'name': 'Электронный документ', 'archived_date': None}, 'type_repeat': {'id': 1, 'value': 'Первичное', 'archived_date': None}, 'document_type': {'id': 86, 'pid': None, 'type_name': 'Служебное письмо', 'archived_date': None}, 'number': 'АМ-4-10458/21 ДСП', 'subjects': [], 'coauthors': [], 'with_out_main_file': None, 'number_was_generated': True, 'auto_incremented': False, 'reserved_number': None, 'reserved_nomenclature': None}

