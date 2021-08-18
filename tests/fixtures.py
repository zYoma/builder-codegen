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
    return {'receiptDate': '2021-08-17T11:36:06+03:00', 'appealDate': None, 'registrationDate': '2021-08-17', 'deadlineDate': None, 'authors': [], 'nomenclature': {}, 'questions': [], 'answers': [], 'files': [], 'pages': [], 'coveringLetters': [], 'appealParticipants': [], 'curators': [], 'resolutionCurators': [], 'employees': [], 'addresseeActingEmployees': [], 'appealObjects': [], 'authorOfLegals': [], 'toNumber': [], 'referringDocuments': [], 'options': {}, 'numberPages': '1+0+1', 'numberSignatures': 1, 'isAdministrativeUse': True, 'documentKind': 'INCOMING', 'medoDocumentKind': None, 'typeReceipt': {}, 'typeRepeat': {}, 'documentType': {}, 'number': 'АМ-4-10314/21 ДСП', 'subjects': [], 'coauthors': [], 'withOutMainFile': None, 'numberWasGenerated': True, 'autoIncremented': False, 'reservedNumber': None, 'reservedNomenclature': None}


@pytest.fixture
def make_code_string_result():
    return '''@dataclass
class TestFormData(BaseModel):
    receiptDate: Optional[str] = None
    appealDate: Optional[str] = None
    registrationDate: Optional[str] = None
    deadlineDate: Optional[str] = None
    authors: Optional[list] = None
    nomenclature: Optional[dict] = None
    questions: Optional[list] = None
    answers: Optional[list] = None
    files: Optional[list] = None
    pages: Optional[list] = None
    coveringLetters: Optional[list] = None
    appealParticipants: Optional[list] = None
    curators: Optional[list] = None
    resolutionCurators: Optional[list] = None
    employees: Optional[list] = None
    addresseeActingEmployees: Optional[list] = None
    appealObjects: Optional[list] = None
    authorOfLegals: Optional[list] = None
    toNumber: Optional[list] = None
    referringDocuments: Optional[list] = None
    options: Optional[dict] = None
    numberPages: Optional[str] = None
    numberSignatures: Optional[int] = None
    isAdministrativeUse: Optional[bool] = None
    documentKind: Optional[str] = None
    medoDocumentKind: Optional[str] = None
    typeReceipt: Optional[dict] = None
    typeRepeat: Optional[dict] = None
    documentType: Optional[dict] = None
    number: Optional[str] = None
    subjects: Optional[list] = None
    coauthors: Optional[list] = None
    withOutMainFile: Optional[str] = None
    numberWasGenerated: Optional[bool] = None
    autoIncremented: Optional[bool] = None
    reservedNumber: Optional[str] = None
    reservedNomenclature: Optional[str] = None


class TestFormDataBuilde(BaseBuilder):
    def __init__(self):
        super().__init__()
        self._receiptDate: Optional[str] = None
        self._appealDate: Optional[str] = None
        self._registrationDate: Optional[str] = None
        self._deadlineDate: Optional[str] = None
        self._authors: Optional[list] = None
        self._nomenclature: Optional[dict] = None
        self._questions: Optional[list] = None
        self._answers: Optional[list] = None
        self._files: Optional[list] = None
        self._pages: Optional[list] = None
        self._coveringLetters: Optional[list] = None
        self._appealParticipants: Optional[list] = None
        self._curators: Optional[list] = None
        self._resolutionCurators: Optional[list] = None
        self._employees: Optional[list] = None
        self._addresseeActingEmployees: Optional[list] = None
        self._appealObjects: Optional[list] = None
        self._authorOfLegals: Optional[list] = None
        self._toNumber: Optional[list] = None
        self._referringDocuments: Optional[list] = None
        self._options: Optional[dict] = None
        self._numberPages: Optional[str] = None
        self._numberSignatures: Optional[int] = None
        self._isAdministrativeUse: Optional[bool] = None
        self._documentKind: Optional[str] = None
        self._medoDocumentKind: Optional[str] = None
        self._typeReceipt: Optional[dict] = None
        self._typeRepeat: Optional[dict] = None
        self._documentType: Optional[dict] = None
        self._number: Optional[str] = None
        self._subjects: Optional[list] = None
        self._coauthors: Optional[list] = None
        self._withOutMainFile: Optional[str] = None
        self._numberWasGenerated: Optional[bool] = None
        self._autoIncremented: Optional[bool] = None
        self._reservedNumber: Optional[str] = None
        self._reservedNomenclature: Optional[str] = None

    def with_receiptDate(self, receiptDate):
        self._receiptDate = receiptDate
        return self

    def with_appealDate(self, appealDate):
        self._appealDate = appealDate
        return self

    def with_registrationDate(self, registrationDate):
        self._registrationDate = registrationDate
        return self

    def with_deadlineDate(self, deadlineDate):
        self._deadlineDate = deadlineDate
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

    def with_coveringLetters(self, coveringLetters):
        self._coveringLetters = coveringLetters
        return self

    def with_appealParticipants(self, appealParticipants):
        self._appealParticipants = appealParticipants
        return self

    def with_curators(self, curators):
        self._curators = curators
        return self

    def with_resolutionCurators(self, resolutionCurators):
        self._resolutionCurators = resolutionCurators
        return self

    def with_employees(self, employees):
        self._employees = employees
        return self

    def with_addresseeActingEmployees(self, addresseeActingEmployees):
        self._addresseeActingEmployees = addresseeActingEmployees
        return self

    def with_appealObjects(self, appealObjects):
        self._appealObjects = appealObjects
        return self

    def with_authorOfLegals(self, authorOfLegals):
        self._authorOfLegals = authorOfLegals
        return self

    def with_toNumber(self, toNumber):
        self._toNumber = toNumber
        return self

    def with_referringDocuments(self, referringDocuments):
        self._referringDocuments = referringDocuments
        return self

    def with_options(self, options):
        self._options = options
        return self

    def with_numberPages(self, numberPages):
        self._numberPages = numberPages
        return self

    def with_numberSignatures(self, numberSignatures):
        self._numberSignatures = numberSignatures
        return self

    def with_isAdministrativeUse(self, isAdministrativeUse):
        self._isAdministrativeUse = isAdministrativeUse
        return self

    def with_documentKind(self, documentKind):
        self._documentKind = documentKind
        return self

    def with_medoDocumentKind(self, medoDocumentKind):
        self._medoDocumentKind = medoDocumentKind
        return self

    def with_typeReceipt(self, typeReceipt):
        self._typeReceipt = typeReceipt
        return self

    def with_typeRepeat(self, typeRepeat):
        self._typeRepeat = typeRepeat
        return self

    def with_documentType(self, documentType):
        self._documentType = documentType
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

    def with_withOutMainFile(self, withOutMainFile):
        self._withOutMainFile = withOutMainFile
        return self

    def with_numberWasGenerated(self, numberWasGenerated):
        self._numberWasGenerated = numberWasGenerated
        return self

    def with_autoIncremented(self, autoIncremented):
        self._autoIncremented = autoIncremented
        return self

    def with_reservedNumber(self, reservedNumber):
        self._reservedNumber = reservedNumber
        return self

    def with_reservedNomenclature(self, reservedNomenclature):
        self._reservedNomenclature = reservedNomenclature
        return self

    def build(self):
        return TestFormData(
            receiptDate=self._receiptDate,
            appealDate=self._appealDate,
            registrationDate=self._registrationDate,
            deadlineDate=self._deadlineDate,
            authors=self._authors,
            nomenclature=self._nomenclature,
            questions=self._questions,
            answers=self._answers,
            files=self._files,
            pages=self._pages,
            coveringLetters=self._coveringLetters,
            appealParticipants=self._appealParticipants,
            curators=self._curators,
            resolutionCurators=self._resolutionCurators,
            employees=self._employees,
            addresseeActingEmployees=self._addresseeActingEmployees,
            appealObjects=self._appealObjects,
            authorOfLegals=self._authorOfLegals,
            toNumber=self._toNumber,
            referringDocuments=self._referringDocuments,
            options=self._options,
            numberPages=self._numberPages,
            numberSignatures=self._numberSignatures,
            isAdministrativeUse=self._isAdministrativeUse,
            documentKind=self._documentKind,
            medoDocumentKind=self._medoDocumentKind,
            typeReceipt=self._typeReceipt,
            typeRepeat=self._typeRepeat,
            documentType=self._documentType,
            number=self._number,
            subjects=self._subjects,
            coauthors=self._coauthors,
            withOutMainFile=self._withOutMainFile,
            numberWasGenerated=self._numberWasGenerated,
            autoIncremented=self._autoIncremented,
            reservedNumber=self._reservedNumber,
            reservedNomenclature=self._reservedNomenclature,
        ).asdict()'''
