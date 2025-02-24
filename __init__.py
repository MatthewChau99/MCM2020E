import Data_Preprocess as dp
import NLP_analysis as nlp
import Data_Manipulation as dm
import Data_Reorganize as dr

if __name__ == '__main__':
    dp.data_preprocess()
    print('------------ Data Preprocessed ------------')
    nlp.nlp()
    print('--------- Data Sentiment Calculated ---------')
    dm.data_manipulate()
    print('------------ Data Calculated ------------')
    dr.data_reorganize()
    print('------------ Data Reorganized ------------')




