import unittest
import UserFunctions
import FinalProject

sheet_id = '1l20PqkNbb3_HmhJprtnLzuWiBWeYkbv6t5RQKZKMtGU'  #<------ Put Sheet ID in the URL here
file_name = 'C:/Users/shado/testscripts/mongan final project/finalproject.csv'
download_google_sheet_as_csv(sheet_id, file_name)
database = generate_database(file_name)

class TestFunctions(unittest.TestCase):

    def test_worker_exists(self):
        retn = worker_exists("asjfhsakgksangjasnkg", database)
        assertEqual(retn, 0)
        ret = worker_exists("Evan Tilton", database)
        assertEqual(ret, 1)
        retall = worker_exists("all", database)
        assertEqual(retall, 2)

    def test_tokenizer(self):
        lines = []
        expected = []
        
        lines.append("pay workername=Evan Tilton")
        expected.append([["pay", "workername=Evan Tilton"],["pay", "workername"]])
        lines.append("pay")
        expected.append([["pay"],["pay"]])
        lines.append("pay jasafkasjg")
        expected.append([["pay"],["pay"]])
        lines.append("hours workername=Evan Tilton")
        expected.append([["hours", "workername=Evan Tilton"],["hours", "workername"]])
        lines.append("hours")
        expected.append([["hours"],["hours"]])
        lines.append("hours jasdkgakjdgka")
        expected.append([["hours"],["hours"]])
        lines.append("update")
        expected.append([["update"],["update"]])
        lines.append("update asjfas")
        expected.append([["update"],["update"]])
        
        lines.append("saijgkasg pay")
        expected.append([["pay"],["pay"]])
        lines.append("451340")
        expected.append([[],[]])
        lines.append(" ")
        expected.append([[],[]])

        runs = 0
        for line of lines:
            tokens, tokentypes = generate_tokens(line)
            assertEqual(expected[runs][0], tokens)
            assertEqual(expected[runs][1], tokentypes)

        

if __name__ == '__main__':
    unittest.main()
