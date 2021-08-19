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
        self._nomenclature: Optional[dict] = {}
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
        self._options: Optional[dict] = {}
        self._number_pages: Optional[str] = None
        self._number_signatures: Optional[int] = None
        self._is_administrative_use: Optional[bool] = None
        self._document_kind: Optional[str] = None
        self._medo_document_kind: Optional[str] = None
        self._type_receipt: Optional[dict] = {}
        self._type_repeat: Optional[dict] = {}
        self._document_type: Optional[dict] = {}
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
