import re
from django.shortcuts import render
# from lexer import MyLexer
# from parser import MyParser
from sly import Lexer
from sly import Parser
ERROR_GLOB = 0
class MyLexer(Lexer):
    # these are set of tokens that are to be exported to the parser
    tokens = {
        SUM,
        COUNT,
        AVG,
        MIN,
        MAX,
        REALNUM,
        INTNUM,
        COL_NAME,
        TABLE_NAME,
        STRING,
        CHARACTER,
        IDENTIFIER,
        EQUAL,
        ADDEQ,
        SUBEQ,
        MULEQ,
        DIVEQ,
        MODEQ,
        GTEQ,
        LTEQ,
        NOTEQ,
        ANDEQ,
        OREQ,
        XOREQ,
        ADDOP,
        SUBOP,
        MULOP,
        DIVOP,
        MODOP,
        GTOP,
        LTOP,
        ANDOP,
        OROP,
        XOROP,
        SEPARATORS,
        SEMICOLON,
        COMMA,
        LCB,
        RCB,
        LFB,
        RFB,
        LSB,
        NAMES,
        NUMS,
        RELOP,
        RSB,
        UPDATE,
        BACKUP,
        FROM,
        DISTINCT,
        LIMIT,
        ORDER,
        ADD,
        DATABASE,
        BETWEEN,
        ASC,
        CASE,
        EXISTS,
        AND,
        TRUNCATE,
        PROCEDURE,
        WHERE,
        VALUES,
        ALL,
        HAVING,
        LIKE,
        EXEC,
        CONSTRAINT,
        COLUMN,
        DEFAULT,
        ROWNUM,
        REPLACE,
        IS,
        SET,
        LEFT,
        AS,
        FULL,
        ALTER,
        RIGHT,
        GROUP,
        INTO,
        SHOW,
        ANY,
        NULL,
        BY,
        INSERT,
        SELECT,
        NOT,
        TABLE,
        KEY,
        USE,
        TOP,
        UNION,
        INNER,
        CHECK,
        JOIN,
        FOREIGN,
        PRIMARY,
        IN,
        UNIQUE,
        VIEW,
        DELETE,
        OUTER,
        VARCHAR,
        OR,
        INDEX,
        DROP,
        CREATE,
        SOME,
        DESC,
        BOOL,
        OFFSET
    }

    # Identifiers and keywords
    IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'

    IDENTIFIER['ADD'] = ADD
    IDENTIFIER['CONSTRAINT'] = CONSTRAINT
    IDENTIFIER['ALTER'] = ALTER
    IDENTIFIER['COLUMN'] = COLUMN
    IDENTIFIER['TABLE'] = TABLE
    IDENTIFIER['AS'] = AS
    IDENTIFIER['ASC'] = ASC
    IDENTIFIER['BACKUP'] = BACKUP
    IDENTIFIER['DATABASE'] = DATABASE
    IDENTIFIER['CASE'] = CASE
    IDENTIFIER['CHECK'] = CHECK
    IDENTIFIER['CREATE'] = CREATE
    IDENTIFIER['INDEX'] = INDEX
    IDENTIFIER['REPLACE'] = REPLACE
    IDENTIFIER['VIEW'] = VIEW
    IDENTIFIER['PROCEDURE'] = PROCEDURE
    IDENTIFIER['UNIQUE'] = UNIQUE
    IDENTIFIER['DEFAULT'] = DEFAULT
    IDENTIFIER['DELETE'] = DELETE
    IDENTIFIER['DESC'] = DESC
    IDENTIFIER['DISTINCT'] = DISTINCT
    IDENTIFIER['DROP'] = DROP
    IDENTIFIER['USE'] = USE
    IDENTIFIER['SHOW'] = SHOW
    IDENTIFIER['EXEC'] = EXEC
    IDENTIFIER['FOREIGN'] = FOREIGN
    IDENTIFIER['KEY'] = KEY
    IDENTIFIER['FROM'] = FROM
    IDENTIFIER['FULL'] = FULL
    IDENTIFIER['OUTER'] = OUTER
    IDENTIFIER['JOIN'] = JOIN
    IDENTIFIER['GROUP'] = GROUP
    IDENTIFIER['BY'] = BY
    IDENTIFIER['HAVING'] = HAVING
    IDENTIFIER['INNER'] = INNER
    IDENTIFIER['INSERT'] = INSERT
    IDENTIFIER['INTO'] = INTO
    IDENTIFIER['SELECT'] = SELECT
    IDENTIFIER['NULL'] = NULL
    IDENTIFIER['IS'] = IS
    IDENTIFIER['LEFT'] = LEFT
    IDENTIFIER['LIMIT'] = LIMIT
    IDENTIFIER['ORDER'] = ORDER
    IDENTIFIER['PRIMARY'] = PRIMARY
    IDENTIFIER['RIGHT'] = RIGHT
    IDENTIFIER['ROWNUM'] = ROWNUM
    IDENTIFIER['TOP'] = TOP
    IDENTIFIER['SET'] = SET
    IDENTIFIER['TRUNCATE'] = TRUNCATE
    IDENTIFIER['UNION'] = UNION
    IDENTIFIER['UPDATE'] = UPDATE
    IDENTIFIER['VALUES'] = VALUES
    IDENTIFIER['WHERE'] = WHERE
    IDENTIFIER['VARCHAR'] = VARCHAR
    IDENTIFIER['ALL'] = ALL
    IDENTIFIER['AND'] = AND
    IDENTIFIER['ANY'] = ANY
    IDENTIFIER['BETWEEN'] = BETWEEN
    IDENTIFIER['EXISTS'] = EXISTS
    IDENTIFIER['IN'] = IN
    IDENTIFIER['LIKE'] = LIKE
    IDENTIFIER['NOT'] = NOT
    IDENTIFIER['OR'] = OR
    IDENTIFIER['SOME'] = SOME
    IDENTIFIER['OFFSET'] = OFFSET
    # EXTRAS
    IDENTIFIER['SUM'] = SUM
    IDENTIFIER['COUNT'] = COUNT
    IDENTIFIER['MIN'] = MIN
    IDENTIFIER['MAX'] = MAX
    IDENTIFIER['AVG'] = AVG

    EQUAL = r'\='
    COMMA = r'\,'

    # Arithmetic Assignment Operators
    ADDEQ = r'\+\='
    SUBEQ = r'\-\='
    MULEQ = r'\*\='
    DIVEQ = r'\/\='
    MODEQ = r'\%\='

    # Comparison Operators
    GTEQ = r'\>\='
    LTEQ = r'\<\='
    NOTEQ = r'\<\>'

    # Bitwise Assignment Operators
    ANDEQ = r'\&\='
    OREQ = r'\|\='
    XOREQ = r'\^\='

    # Arithmetic Operators
    ADDOP = r'\+'
    SUBOP = r'\-'
    MULOP = r'\*'
    DIVOP = r'\/'
    MODOP = r'\%'

    # Comparison Operators
    GTOP = r'\>'
    LTOP = r'\<'

    # Bitwise Operators
    ANDOP = r'\&'
    OROP = r'\|'
    XOROP = r'\^'

    SEPARATORS = r'\,'
    SEMICOLON = r'\;'
    LCB = r'\('
    RCB = r'\)'
    LFB = r'\{'
    RFB = r'\}'
    LSB = r'\['
    RSB = r'\]'

    INTNUM = r'\d+'
    REALNUM = r'\d+.\d+'
    # Should String Have New Line OR NOT..? Problematic
    # \'.*\' matches longest so in between thing cannot be \' .......That's all
    STRING = r'\'([ \t\n\r\f\v]|[^ \'\t\n\r\f\v])+\''
    # STRING = r'\'.*\''
    # @_(r'''("[^"\\]*(\\.[^"\\]*)*"|'[^'\\]*(\\.[^'\\]*)*')''')

    ignore = r'\t '

    def IDENTIFIER(self, t):
        return t

    @_('TRUE')
    def BOOL(self, t):
        t.value = 1
        return t

    @_('FALSE')
    def BOOL(self, t):
        t.value = 0
        return t

    # @_('UNKNOWN')
    # def BOOL(self,t):
    #     t.value=-
    #     return t

    def INTNUM(self, t):
        t.value = int(t.value)
        return t

    def REALNUM(self, t):
        t.value = float(t.value)
        return t

    # @_(r'''('\d+'|'\\d+.\d+')''')
    # def NUMS(self, t):
    #     return t

    def STRING(self, t):
        l = len(t.value)
        t.value = t.value[1:(l - 1)]
        try:
            t.value = int(t.value)
            t.type = 'INTNUM'
        except ValueError:
            try:
                t.value = float(t.value)
                t.type = 'REALNUM'
            except ValueError:
                t.type = 'STRING'
        return t

    # ignore_comment = r'\#.*'
    @_(r'#.*')
    def COMMENT(self, t):
        pass

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    def error(self, t):
        print('Line %d: Bad Character -> %r' % (self.lineno, t.value[0]))
        self.index += 1


class Query():
    # Specs = {}
    # ColumnList = []
    # ValueList = []
    list_of_op = ['=', '<', '<=', '>', '>=', '<>']
    list_of_logicOp = ['and', 'or', 'not']

    def __init__(self):
        self.Specs = {}
        self.ColumnList = []
        self.ValueList = []

    # def convertCode()
    def debugStructure(self):
        print(self.Specs)
        print(self.ColumnList)
        print(self.ValueList)

    def clearStructure(self):
        self.Specs = {}
        self.ColumnList = []
        self.ValueList = []

    def addToColumnList(self, column_name):
        # check for duplicates
        if (column_name in self.ColumnList):
            return
        self.ColumnList.append(column_name)

    def addToValueList(self, value):
        self.ValueList.append(value)

    def createQueryBaseCase(self, tup):
        if (tup[0] == '='):
            return "{\"" + tup[1] + "\" :" + str(tup[2]) + "}"
        elif (tup[0] == '<'):
            return "{\"" + tup[1] + "\" : { \"$lt\" :" + str(tup[2]) + "}" + "}"
        elif (tup[0] == '<='):
            return "{\"" + tup[1] + "\" : { \"$lte\" :" + str(tup[2]) + "}" + "}"
        elif (tup[0] == '>'):
            return "{\"" + tup[1] + "\" : { \"$gt\" :" + str(tup[2]) + "}" + "}"
        elif (tup[0] == '>='):
            return "{\"" + tup[1] + "\" : { \"$gte\" :" + str(tup[2]) + "}" + "}"
        elif (tup[0] == '<>'):
            return "{\"" + tup[1] + "\" : { \"$ne\" :" + str(tup[2]) + "}" + "}"

    def createQueryParameter(self, cond_tree):
        # For Where Clause and stuff
        if (cond_tree == ''):
            return '{' + '}'

        if (cond_tree[0] in self.list_of_op):
            # base case
            return self.createQueryBaseCase(cond_tree)
        elif (cond_tree[0] in self.list_of_logicOp):
            q1 = self.createQueryParameter(cond_tree[1])
            q2 = self.createQueryParameter(cond_tree[2])
            return "{ $" + cond_tree[0] + " : [" + q1 + ',' + q2 + ']}' 
        return '{' + '}'

    def createProjectParameter(self):
        # For Select Parameter -> selecting certain columns
        print("col list " + str(self.ColumnList))
        if ("*" in self.ColumnList):
            print("project parameter empty")
            return ''
        else:
            pairs = []
            for col in self.ColumnList:
                pairs.append(f'\"{col}\":{1}')
            pairs.append(f'\"_id\":{1}')
            s = ','
            s = s.join(pairs)
            print("project parameter" + '{' + s + '}')
            return '{' + s + '}'

    def createInsertParameter(self):
        # For insert statement
        if (len(self.ColumnList) != len(self.ValueList)):
            return "Error! Query is Wrong.. Either duplicate column or non-matching length of columns and values"
        pairs = []
        for col, val in zip(self.ColumnList, self.ValueList):
            pairs.append(f'\"{col}\":{val}')
        s = ','
        s = s.join(pairs)
        print("insert parameter" + '{' + s + '}')
        return '{' + s + '}'

    def createUpdateParameter(self):
        # For Update Parameter
        if (len(self.ColumnList) != len(self.ValueList)):
            return "Error! Query is Wrong.. non-matching length of columns and values"
        pairs = []
        for col, val in zip(self.ColumnList, self.ValueList):
            pairs.append(f'\"{col}\":{val}')
        s = ','
        s = s.join(pairs)
        # print("update parameter-" + '{$set:{' + s + '},' + '{' + "multi:true" +'}' + '}'
        return '{$set:{' + s + '},' + '{' + "multi:true" +'}' + '}'

    def createAggregateParameter(self):
        # For Things like sum avg etc..
        # Dont know scope
        return

    def convertStructToCode(self):
        obj = self.Specs
        if ('type' not in obj):
            return 'Error!! Query is Wrong'

        if (obj['type'] == 'insert'):
            insert_param = self.createInsertParameter()
            return "db." + obj['table_name'] + ".insert(" + insert_param + ')'
        elif (obj['type'] == 'update'):
            update_param = self.createUpdateParameter()
            query_param = self.createQueryParameter(obj['update_cond_tree'])
            return "db." + obj['table_name'] + ".updateMany(" + query_param + ',' + update_param + ')'
        elif (obj['type'] == 'delete'):
            query_param = self.createQueryParameter(obj['delete_cond_tree'])
            return "db." + obj['table_name'] + ".remove(" + query_param + ')'
        elif (obj['type'] == 'select'):
            project_param = self.createProjectParameter()
            query_param = self.createQueryParameter(obj['select_cond_tree'])
            # print(project_param)
            # print(query_param)
            if (obj['is_aggr'] == 0):
                if (not project_param):
                    return "db." + obj['table_name'] + ".find(" + query_param + ')'
                else:
                    return "db." + obj['table_name'] + ".find(" + query_param + ',' + project_param + ')'
        return ''


Q = Query()
list_of_queries = []


class MyParser(Parser):
    tokens = MyLexer.tokens

    precedence = (
        ('left', "OR"),
        ('left', "AND"),
        ('left', "NOT"),
    )
    start = 'start1'

    # start - query_list
    @_('query_list')
    def start1(self, p):
        return (p[0], list_of_queries)

    # query_list - query query_list
    @_('query query_list')
    def query_list(self, p):
        # Q.convertCode()
        Q.debugStructure()
        list_of_queries.append(Q.convertStructToCode())
        Q.clearStructure()
        return p[0]

    @_('empty')
    def query_list(self, p):
        return

    @_('')
    def empty(self, p):
        pass

    @_('select_stmt SEMICOLON')
    def query(self, p):
        Q.Specs["type"] = "select"
        return "SELECT_STATEMENT"

    @_('update_stmt SEMICOLON')
    def query(self, p):
        Q.Specs["type"] = "update"
        return "UPDATE_STATEMENT"

    @_('insert_stmt SEMICOLON')
    def query(self, p):
        Q.Specs["type"] = "insert"
        return "INSERT_STATEMENT"

    @_('delete_stmt SEMICOLON')
    def query(self, p):
        Q.Specs["type"] = "delete"
        return "DELETE_STATEMENT"

    # --------------- INSERT STATEMENT ---------------
    @_('INSERT INTO IDENTIFIER LCB insert_col_list RCB VALUES LCB val_list RCB')
    def insert_stmt(self, p):
        Q.Specs["table_name"] = p[2]
        return

    @_('insert_col_list COMMA IDENTIFIER')
    def insert_col_list(self, p):
        Q.addToColumnList(p[2])
        # print("Id Printed", p[2])
        return

    @_('IDENTIFIER')
    def insert_col_list(self, p):
        Q.addToColumnList(p[0])
        # print("One Id Printed", p[0])
        return

    @_('val_list COMMA value')
    def val_list(self, p):
        Q.addToValueList(p[2])
        return

    @_('value')
    def val_list(self, p):
        Q.addToValueList(p[0])
        return

    # --------------- INSERT STATEMENT ---------------

    # --------------- SELECT STATEMENT ---------------
    @_('SELECT is_distinct select_param FROM IDENTIFIER select_opt_where sort_order opt_limit')
    def select_stmt(self, p):
        Q.Specs["table_name"] = p[4]
        Q.Specs["select_cond_tree"] = p[5]
        return

    @_('DISTINCT')
    def is_distinct(self, p):
        Q.Specs["is_distinct"] = 1
        return

    @_('')
    def is_distinct(self, p):
        Q.Specs["is_distinct"] = 0
        return

    @_('select_col_list')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.Specs["is_aggr"] = 0
        return

    @_('MULOP')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.addToColumnList('*')
        Q.Specs["is_aggr"] = 0
        return

    @_('MAX LCB IDENTIFIER RCB')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.Specs["is_aggr"] = 1
        Q.Specs["aggr"] = "MAX"
        Q.Specs["aggr_list"] = p[2]
        return

    @_('MIN LCB IDENTIFIER RCB')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.Specs["is_aggr"] = 1
        Q.Specs["aggr"] = "MIN"
        Q.Specs["aggr_list"] = p[2]
        return

    @_('COUNT LCB IDENTIFIER RCB')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.Specs["is_aggr"] = 1
        Q.Specs["aggr"] = "COUNT"
        Q.Specs["aggr_list"] = p[2]
        return

    @_('COUNT LCB MULOP RCB')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.Specs["is_aggr"] = 1
        Q.Specs["aggr"] = "COUNT"
        Q.Specs["aggr_list"] = p[2]
        return

    @_('SUM LCB IDENTIFIER RCB')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.Specs["is_aggr"] = 1
        Q.Specs["aggr"] = "SUM"
        Q.Specs["aggr_list"] = p[2]
        return

    @_('AVG LCB IDENTIFIER RCB')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.Specs["is_aggr"] = 1
        Q.Specs["aggr"] = "AVG"
        Q.Specs["aggr_list"] = p[2]
        return

    @_('select_col_list COMMA IDENTIFIER opt_aliasing')
    def select_col_list(self, p):
        Q.addToColumnList(p[2])
        if (p[3] != ''):
            Q.Specs['alias_map'][p[2]] = p[3]
        return

    @_('IDENTIFIER opt_aliasing')
    def select_col_list(self, p):
        Q.addToColumnList(p[0])
        Q.Specs['alias_map'] = {}
        if (p[1] != ''):
            Q.Specs['alias_map'][p[0]] = p[1]
        return

    @_('AS IDENTIFIER')
    def opt_aliasing(self, p):
        return p[1]

    @_('')
    def opt_aliasing(self, p):
        return ''

    @_('WHERE condition_list')
    def select_opt_where(self, p):
        return p[1]

    @_('IDENTIFIER IS NULL')
    def condition(self, p):
        return ('=', p[0], '')

    @_('IDENTIFIER IS NOT NULL')
    def condition(self, p):
        return ('<>', p[0], '')

    @_('')
    def select_opt_where(self, p):
        return ''

    @_('NOT condition_list')
    def condition_list(self, p):
        return ('not', p[1])

    @_('condition_list AND condition_list')
    def condition_list(self, p):
        return ('and', p[0], p[2])

    @_('condition_list OR condition_list')
    def condition_list(self, p):
        return ('or', p[0], p[2])

    @_('condition')
    def condition_list(self, p):
        return p[0]

    @_('IDENTIFIER EQUAL value', 'IDENTIFIER GTEQ value', 'IDENTIFIER LTEQ value', 'IDENTIFIER GTOP value',
       'IDENTIFIER LTOP value', 'IDENTIFIER NOTEQ value')
    def condition(self, p):
        # print(p[0],p[1],p[2])
        return (p[1], p[0], p[2])

    @_('LCB condition_list RCB')
    def condition(self, p):
        return (p[1])

    @_('ORDER BY ASC')
    def sort_order(self, p):
        Q.Specs["sort_order"] = 0
        return

    @_('ORDER BY DESC')
    def sort_order(self, p):
        Q.Specs["sort_order"] = 1
        return

    @_('')
    def sort_order(self, p):
        Q.Specs["sort_order"] = 0
        return

    @_('LIMIT INTNUM opt_offset')
    def opt_limit(self, p):
        Q.Specs["limit_value"] = p[1]
        return

    @_('')
    def opt_limit(self, p):
        return

    @_('OFFSET INTNUM')
    def opt_offset(self, p):
        Q.Specs["offset"] = p[1]
        return

    @_('')
    def opt_offset(self, p):
        return

    # --------------- SELECT STATEMENT ---------------

    # --------------- DELETE STATEMENT ---------------
    @_('DELETE FROM IDENTIFIER delete_opt_where')
    def delete_stmt(self, p):
        Q.Specs["table_name"] = p[2]
        # Either Empty or a tree of tuple as a node
        Q.Specs["delete_cond_tree"] = p[3]
        return

    @_('WHERE condition_list')
    def delete_opt_where(self, p):
        return p[1]

    @_('')
    def delete_opt_where(self, p):
        return ""

    # --------------- DELETE STATEMENT ---------------

    # --------------- UPDATE STATEMENT ---------------

    @_('UPDATE IDENTIFIER SET col_assigns select_opt_where')
    def update_stmt(self, p):
        Q.Specs["table_name"] = p[1]
        # Either Empty or a tree of tuple as a node
        Q.Specs["update_cond_tree"] = p[4]
        return

    @_('col_assigns COMMA col_assign')
    def col_assigns(self, p):
        return

    @_('col_assign')
    def col_assigns(self, p):
        return

    @_('column_name EQUAL value')
    def col_assign(self, p):
        # adding column = value for update parameter
        Q.addToColumnList(p[0])
        Q.addToValueList(p[2])
        return

    @_('IDENTIFIER')
    def column_name(self, p):
        return p[0]

    @_('INTNUM', 'REALNUM')
    def value(self, p):
        # Q.addToValueList(p[0])
        # print("One val Printed", p[0])
        # print(p[0].type)
        # try:
        #     print(p.STRING)
        #     print("Issue with String")
        # except ValueError:
        #     print("PROBLEM")
        return p[0]

    @_('STRING')
    def value(self, p):
        return "\"" + p[0] + "\""

    # --------------- UPDATE STATEMENT ---------------

    def error(self, p):
        if p:
            print("Syntax error at token", p.type, p.value)
            # Just discard the token and tell the parser it's okay.
            # self.errok()
            ERROR_GLOB = 1
        else:
            print("Syntax error at EOF")

# Create your views here.
def frontend(request):
    query=""
    input = ""
    if 'clear' in request.POST:
        return render(request, 'index.html', {'querystr':"",'value':""})
    if request.POST.get('query'):
        query = request.POST.get('query')
        print("query is ", query)
        input = query
    list_of_queries.clear()
    lex = MyLexer()
    par = MyParser()
    print(input)
    # while True:
    try:
        # text = input(' Input > ')
        selectText = '''SELECT abc,cde AS aliases FROM Something WHERE KEKE > 10 OR Top > 50 AND (somee =10 OR kake = 2000);'''
        deleteText = '''DELETE FROM TAEEE;'''
        tokenTester = '''
        INSERT INTO GG (col1,col2,col3,col4,col5) VALUES (10,'asfasfasf',30,40,50);'''
        updateTester = '''
        UPDATE Customers
        SET ContactName='Juan',jj='sine' WHERE Country<'Mexico';'''
        someString = '''
        SELECT a,b,c FROM TAB2 WHERE a=1,b=2,c=3;'''
        Q.clearStructure()
        ERROR_GLOB = 0
        result = par.parse(lex.tokenize(input))
        print(result)
        try:
            if(ERROR_GLOB == 1):
                query = input + '\n\n\n' + 'The given query is unsupported or wrong'
            print(list_of_queries)
            query = list_of_queries[0]
        except:
            pass
    except EOFError:
        print("EOF Error")
    return render(request, 'index.html', {'querystr':input,'value':query})