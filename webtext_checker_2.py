import difflib
file1 = r"C:\Users\A0702779\OneDrive - Aon\Desktop\file1.txt"
file2 = r"C:\Users\A0702779\OneDrive - Aon\Desktop\file2.txt"
f1_open = open(file1).readlines()
f2_open = open(file2).readlines()
diff = difflib.HtmlDiff().make_file(f1_open, f2_open, file1, file2)
difference_report = open(r'C:\Users\A0702779\OneDrive - Aon\Desktop\result.html', 'w')
difference_report.write(diff)
difference_report.close()