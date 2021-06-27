import os #operation system

 #讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f: 
		for line in f:
			lines.append(line.strip()) 
		return lines

def convert(lines):
	new = []
	person = None   #定義person初始值
	for line in lines:
		if line == 'Allen':
			person = 'Allen' #現在說話的人是Allen, 記錄下來
			continue         #如果這行完全等於Allen, 跳回for line in lines (進行下一個迴圈 -> 下一個留言)
		elif line == 'Tom':
			person = 'Tom'   #現在說話的人是Tom, 記錄下來
			continue         #如果這行完全等於Tom, 跳回for line in lines (進行下一個迴圈 -> 下一個留言)
		if person:           #若person有值的話, 才做把留言加person
			new.append(person + ': ' + line)  #裝進去new
	return new


def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8') as f:           
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('input.txt')
	#print(lines)
	lines = convert(lines)
	write_file('output.txt', lines)
	#print(lines)

main()