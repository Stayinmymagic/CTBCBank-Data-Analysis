# 中國信託數據建模專案

#### -- Project Status: [Completed]

## Project Intro/Objective
希望透過銀行內部結合外部數據，建立新戶/低地往來戶的財富度評估標準。
利用新戶提供的資訊，預估未來他的資產成長幅度，作為房貸等金融產品的潛力客戶辨識依據。

### Partner
* [中國信託數據研究發展中心]

### Methods Used
* Inferential Statistics
* Descriptive Statistics
* Machine Learning
* Data Visualization
* Predictive Modeling

### Technologies
* Python
* Spyder

### Library
* Pandas
* Numpy
* Stats
*
## Project Description
1.	篩選重要變數：內部資料包含客戶主檔、存款主檔、貸款主檔等，但因本次研究希望可以將新戶依特徵分類，新戶可提供的資料有限，新戶資料較完全的檔為客戶主檔，因此初步篩選資料以客戶主檔的變數著手，針對不同類型的資料使用相關分析、卡方分析、變異數分析等敘述統計方法選出對資產有顯著影響的資料。(使用stats and scikit-learn模組)
2.	由於我們希望尋找與新戶相關資料，幫助我們對客戶特徵描繪更清楚，資訊更充足，因此外部資料主要是透過網站擷取全國最大的論壇PTT的租屋版資訊，尋找有房產的客戶，最重要的資訊是房東留下的電話，電話是作為與行內資料合併的主鍵，若是有對應的客戶將他視為有房地產的客戶。(使用requests and Beautifulsoup模組)
3.	銀行內部資料有記錄客戶職業別與職位別，但是並沒有實際薪資的資料(因一個人可以有多個帳戶，中國信託帳戶不一定是固定薪資轉帳的帳戶)。因此我們找到主計處薪資統計資料，與行內資料對應，但是主計處統計資料的職業與產業別與銀行內部資料並非完全相同，也就是說，需要靠人工比對才能找出客戶的平均薪資，由於此項工程過於費時，我們透過自然語言處理的Word2vec進行文字模糊比對，從主計處資料找出相對應的薪資並填入銀行內部資料。
4.	這項計畫的目的是建立客戶財富度模型，我們以財富級距作為應變數，整合重要變數以及外部資料做數據建模，嘗試了邏輯斯迴歸、決策樹、隨機森林與類神經網路，但是效果不佳，正確率很高，但是只集中在第一類(財富級距為0-50萬)，其他類正確率皆很低，原因是數據不平衡，舊有的客戶當中有將近七成的用戶是落在此級距，因此成效不彰。
5.	最後，我們選擇放下原本訂立的財富分級，利用非監督式學習的K-means分析，將客戶依其特徵分成16群。每一群在年齡、月收入、總資產方面都有其特徵，例如：年齡40歲左右，月薪約三萬，總資產約八億，將此群推測為富二代。


