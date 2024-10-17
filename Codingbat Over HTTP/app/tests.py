from django.test import TestCase

class TestNearHundred(TestCase):
    def test_near_100(self):
        response = self.client.get("/warmup-1/near-hundred/100/")
        self.assertContains(response, True)
    
    def test_near_150(self):
        response = self.client.get("/warmup-1/near-hundred/150/")
        self.assertContains(response, False)
    
    def test_near_210(self):
        response = self.client.get("/warmup-1/near-hundred/210/")
        self.assertContains(response, True)



class TestStringSplosion(TestCase):
    def test_Code(self):
        response = self.client.get("/warmup-2/string-splosion/Code/")
        self.assertContains(response, "CCoCodCode")

    def test_abc(self):
        response = self.client.get("/warmup-2/string-splosion/abc/")
        self.assertContains(response, "aababc")
    
    def test_ab(self):
        response = self.client.get("/warmup-2/string-splosion/ab/")
        self.assertContains(response, "aab")



class TestCatDog(TestCase):
    def test_catdog(self):
        response = self.client.get("/string-2/cat-dog/catdog/")
        self.assertContains(response, True)

    def test_catcat(self):
        response = self.client.get("/string-2/cat-dog/catcat/")
        self.assertContains(response, False)

    def test_1cat1cadodog(self):
        response = self.client.get("/string-2/cat-dog/1cat1cadodog/")
        self.assertContains(response, True)



class TestLoneSum(TestCase):
    def test_123(self):
        response = self.client.get("/logic-2/lone-sum/1/2/3/")
        self.assertContains(response, 6)

    def test_323(self):
        response = self.client.get("/logic-2/lone-sum/3/2/3/")
        self.assertContains(response, 2)
    
    def test_333(self):
        response = self.client.get("/logic-2/lone-sum/3/3/3/")
        self.assertContains(response, 0)