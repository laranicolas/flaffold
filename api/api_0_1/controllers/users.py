from controllers import Controllers


class Users(Controllers):

    exclude_columns = ['password']

    @staticmethod
    def get_single_postprocessor(result=None, **kw): 
        if 'phone' in result and 'area_code' in result:
            result['code_phone'] = '{0}-{1}'.format(
                result['area_code'],
                result['phone']
            )