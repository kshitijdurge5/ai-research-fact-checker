from app import review_claim

def test_no_evidence_not_verified(): assert 'UNVERIFIED' in review_claim('Claim','')['status']
def test_evidence_not_overclaimed(): assert 'not independently verified' in review_claim('Claim','Source text')['status']
