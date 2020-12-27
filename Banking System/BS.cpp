#include <iostream>
#include <fstream>
#include <string>

#define ll long long int

using namespace std;

bool file_empty()
{
	ifstream read("Data.txt");
	bool isEmpty = read.peek() == EOF;
	read.close();
	return isEmpty;
}


class Bank
{
public:
	void OpenAccount(string fname, string lname,ll  uid,ll  deposit);
	void Balance_enquiry(ll acc_num);
	void View_Data(string file_name);
	void withdrawl(ll w_AccNum);
	void Deposit(ll deposit_amount);
	ll get_current_acc();
};

void Bank::OpenAccount(string fname, string lname, ll  uid, ll  deposit)
{
	Bank b;
	ll acc_num = b.get_current_acc();
	acc_num++;
	cout << "Congratulations " << fname << " " << lname << " for opening an account " << endl;
	cout << "Your Account Number: "<< acc_num << " Balance is Rs " << deposit << "." << endl << endl;

	//open the default data file named with Data.txt
	ofstream outfile("Data.txt",ios::app);
	outfile << "Account Number: " << acc_num << endl;
	outfile << "First Name: " << fname << endl;
	outfile << "Last Name: " << lname << endl;
	outfile << "UID: " << uid << endl;
	outfile << "Deposit: " << deposit << endl;
	outfile.close();
	//close the file
}

ll Bank::get_current_acc()
{

	if (!file_empty())
	{
		//open the file Data for account numbers
		ifstream infile;
		infile.open("Data.txt");


		ll i = 0, myint = 0;
		string text = "";
		string a = "Account Number: ";
		while (getline(infile, text))
		{
			i++;
			if (i == 1 || i % 5 == 1)
			{
				if (text[0] == 'A')
				{
					string mystr = "";
					for (ll j = 0; j < text.size(); j++)
					{
						if (text[j] != a[j])
							mystr += text[j];
					}
					myint = stoi(mystr);
				}
			}
		}
		infile.close();
		return myint;
	}
	else
		cout << "No Data in the File\n";
}

void Bank::Balance_enquiry(ll acc_num)
{
	if (!file_empty())
	{
		//opening the file Data
		ifstream infile;
		infile.open("Data.txt");
		string str_acc_num = to_string(acc_num);
		string find = "Account Number: ";
		find += str_acc_num;
		string text, find2 = "Deposit: ";
		bool flag = false;
		ll myint = 0;
		while (getline(infile, text))
		{
			if (text == find)
			{
				flag = true;
			}
			if (text[0] == 'D' && flag != false)
			{
				string mystr = "";
				for (ll j = 0; j < text.size(); j++)
				{
					if (j >= 9)
						mystr += text[j];
				}
				myint = stoi(mystr);
				if (myint != 0)
					break;
				else
					continue;
			}
		}
		cout << "Balance = " << myint << endl;
		infile.close();
	}
	else
		cout << "No Data in the File\n";
}

void Bank::View_Data(string file_name)
{
	if (!file_empty)
	{
		//open the text file 
		file_name += ".txt";
		ifstream infile;
		infile.open(file_name);
		while (1)
		{
			if (infile)
			{
				string text = "";
				ll i = 0;
				while (getline(infile, text))
				{
					i++;
					if (i == 5)
					{
						cout << text << endl;
						cout << endl;
						i = 0;
					}
					else
						cout << text << endl;
				}
				break;
			}
			else
			{
				cout << "File does not exists! " << endl;
				cout << "Enter the file name or press 1";
				cin >> file_name;
				if (file_name == "1")
					break;
				else
					continue;
			}
		}
		infile.close();
	}
	else
		cout << "No Data in the File\n";
	
}

void Bank::withdrawl(ll w_AccNum)
{
	if (!file_empty())
	{
		ll amount = 0;
		cout << "Enter the amount to be withdrawl : ";
		cin >> amount;

		//opening the files in two places;
		ifstream infile;
		infile.open("Data.txt");

		string text, mystr, find = "Account Number: ";
		find += to_string(w_AccNum);

		bool flag = false;
		ll i = 0;
		while (getline(infile, text))
		{
			if (text == find)
				flag = true;
			if (flag)
			{
				i++;
				if (i == 5)
				{
					for (ll j = 0; j < text.size(); j++)
					{
						if (j > 8)
							mystr += text[j];
					}
				}
				else if (i > 5)
					break;
			}
		}
		infile.close();


		ll myint = stoi(mystr);
		string to_find = "Deposit: ";
		to_find += mystr;

		if (myint < amount)
			cout << "Insufficient balance " << endl << "Balance = " << myint << endl;
		else
		{
			ofstream outfile("Data1.txt", ios::app);
			ifstream new_file;
			new_file.open("Data.txt");
			text = "";
			flag = 0;
			while (getline(new_file, text))
			{
				if (text == to_find && flag == 0)
				{
					string input = "Deposit: ";
					input += to_string(myint - amount);
					outfile << input << endl;
					flag = true;
				}
				else
				{
					outfile << text << endl;
				}
			}

			outfile.close();
			new_file.close();

			char old_name[] = "Data1.txt", new_name[] = "Data.txt";
			remove("Data.txt");
			ll val = rename(old_name, new_name);
		}

	}
	else
		cout << "No Data in the File\n";
}

void Bank::Deposit(ll deposit_account)
{
	if (!file_empty())
	{
		ll deposit_amount = 0;
		cout << "Enter the amount to be deposited : ";
		cin >> deposit_amount;
		string to_find = "Account Number: ";
		to_find += to_string(deposit_account);


		//open the file data
		ifstream infile;
		infile.open("Data.txt");
		string text = "";
		bool flag = 0;
		ll i = 0, myint = 0;
		while (getline(infile, text))
		{
			if (text == to_find)
			{
				flag = true;
			}
			if (text[0] == 'D' && flag != false)
			{
				string mystr = "";
				for (ll j = 0; j < text.size(); j++)
				{
					if (j >= 9)
						mystr += text[j];
				}
				myint = stoi(mystr);
				if (myint != 0)
					break;
				else
					continue;
			}
		}
		infile.close();
		deposit_amount += myint;

		ofstream outfile("Data1.txt", ios::app);
		ifstream new_file;
		new_file.open("Data.txt");
		text = "";
		flag = 0;

		string to_find1 = "Deposit: ";
		to_find1 += to_string(myint);

		while (getline(new_file, text))
		{
			if (text == to_find1 && flag == 0)
			{
				string input = "Deposit: ";
				input += to_string(deposit_amount);
				outfile << input << endl;
				flag = true;
			}
			else
			{
				outfile << text << endl;
			}
		}

		cout << "Successfully deposited!" << endl << "Current Balance = " << deposit_amount << endl;

		outfile.close();
		new_file.close();

		char old_name[] = "Data1.txt", new_name[] = "Data.txt";
		remove("Data.txt");
		ll val = rename(old_name, new_name);
	}
	else
		cout << "No Data in the File\n";
}

int main(void)
{
	
	short choice = 0;
	Bank b;
	do
	{
		cout << "*******************************" << endl;
		cout << "\t**BANKING SYSTEM**" << endl;
		cout << "\t\t1.Open an Account" << endl;
		cout << "\t\t2.Balance Enquiry" << endl;
		cout << "\t\t3.View Data " << endl;
		cout << "\t\t4.Withdrawl" << endl;
		cout << "\t\t5.Deposit" << endl;
		cout << "\t\t6.Quit" << endl;
		cout << "*******************************" << endl;
		cout << "Enter the choice " << endl;
		cin >> choice;

		string lname, fname, file_name;
		ll uid, deposit, acc_num, w_AccNum , deposit_account;

		switch (choice)
		{
			case 1:
				cout << "Enter the First Name ";
				cin >> fname;
				cout << "Enter the Last Name ";
				cin >> lname;
				cout << "Enter the UID ";
				cin >> uid;
				cout << "Enter the Deposit amount ";
				cin >> deposit;
				b.OpenAccount(fname, lname, uid, deposit);
				break;
			case 2:
				cout << "Enter the Account Number: ";
				cin >> acc_num;
				b.Balance_enquiry(acc_num);
				break;
			case 3:
				cout << "Enter the Data file name without txt extension: ";
				cin >> file_name;
				b.View_Data(file_name);
				break;
			case 4: 
				w_AccNum = 0;
				cout << "Enter the Account Number : ";
				cin >> w_AccNum;
				b.withdrawl(w_AccNum);
				break;
			case 5:
				deposit_account = 0;
				cout << "Enter the Account Number: ";
				cin >> deposit_account;
				b.Deposit(deposit_account);
				break;
			case 6:
				cout << "Thanks for Visiting " << endl;
				break;
			default: 
				cout << "Invalid Option, please try again" << endl;
				break;
		}
	} while (choice != 6);
}