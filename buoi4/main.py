#bai1
def normalize_name(text):
    return " ".join(text.split()).title()

print(normalize_name("  Nguyễn   An  "))
print(normalize_name("minh"))
print(normalize_name("   "))

#bai2
def average_score(scores):
    if not scores:
        return None
    return sum(scores) / len(scores)
def count_passed(scores, threshold=5):
    return sum(1 for s in scores if s >= threshold)
test_cases = [[8, 4, 9, 5], [5], []]
for scores in test_cases:
    avg = average_score(scores)
    passed_default = count_passed(scores)
    passed_8 = count_passed(scores, threshold=8)
    print(f"Danh sach diem: {scores}")
    print(f"Diem trung binh: {avg}")
    print(f"So diem dat nguong 5: {passed_default}")
    print(f"So diem dat nguong 8: {passed_8}")
    print("")

#bai3
def rank_students(score_by_name: dict) -> dict:
    sorted_items = sorted(score_by_name.items(), key=lambda item: (-item[1], item[0]))
    return dict(sorted_items)
score_by_name = {"Minh": 9, "Lan": 7, "An": 9, "Vy": 5}
print("Dict an dau:", score_by_name)
ranked = rank_students(score_by_name)
print("Dict sau khi xep hang:", ranked)
print("Kiem tra dict ban dau khong doi:", score_by_name)
print("Dict rong:", rank_students({}))