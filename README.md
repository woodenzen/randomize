# The Archive Random Functions
Install along with archive_path.py wih is the function that will identify the path to your active The Archive directory.

## Usage (Example)
## 1. zkrandom.py
- call zkrand(5) - the number specifies the number of random notes returned.
- output is in a clickable Markdown link. 
### Sample Output
```
[C-ENGL473 January 26, 2021](thearchive://match/C-ENGL473 January 26, 2021 202101211655)
[Writer's Notes](thearchive://match/Writer's Notes 202004202104)
[Warm Glow Of Good Feelings](thearchive://match/Warm Glow Of Good Feelings 201912311756)
[B-Humankind A Hopeful History](thearchive://match/B-Humankind A Hopeful History 202008131131)
[Bardo](thearchive://match/Bardo 201901301829)
```
## 2. rand_with_year.py
- call rand_with_year(10) - the number specifies the number of random notes returned
- output is in a clickable Markdown link. 
### Sample Output
```
## 10 random notes from the past.
2021 [Luxury Beliefs](thearchive://match/Luxury Beliefs 202109220751)
2023 [Desire Path - Social Trail](thearchive://match/Desire Path - Social Trail 202305221607)
2022 [Create a Toggle Switch](thearchive://match/Create a Toggle Switch 202207301507)
2020 [Primary Creative Projects](thearchive://match/Primary Creative Projects 202005030842)
2019 [Something towards nothing](thearchive://match/Something towards nothing 201906060702)
2020 [Waters Of March](thearchive://match/Waters Of March 202008222109)
2020 [Measurement Of A Circle](thearchive://match/Measurement Of A Circle 202002210514)
2023 [A-What Do Human Beings Need?](thearchive://match/A-What Do Human Beings Need? 202305271716)
2019 [Liberate even the antidote](thearchive://match/Liberate even the antidote 201901240524)
2022 [How-to: Annotate like a pro](thearchive://match/How-to: Annotate like a pro 202211240933)
```


## 3. rand_size.py
- call rand_size(800, 1400, 6) - specifying the min word count, max word count, and number of random notes returned
### Sample Output
```
B-Down and Out 202302101625 has 1077 words.
Welcome to The Archive 201902010000 has 1223 words.
Editing Checklist 202002081650 has 846 words.
Tools for thought: science, design, art, craftsmanship 202201011020 has 877 words.
Transference 202301081245 has 899 words.
A-On Food and Happiness 202302082008 has 877 words.
```


## Licience
[MIT](./LICENSE.md)


## Disclaimer
When it comes to Python, I am just a hobbyist. So it's very likely I made some mistakes. Please bear with me. Let me know and I'll fix things and in doing so, you'll be teaching me to be a better programmer.
