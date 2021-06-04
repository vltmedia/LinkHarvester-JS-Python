from .BaseOptions import BaseOptions


class InternetArchiveOptions(BaseOptions):
    """This class includes test options.

    It also includes shared options defined in BaseOptions.
    """

    def initialize(self, parser):
        parser = BaseOptions.initialize(self, parser)  # define shared options
        parser.add_argument('--collection', type=str, required=True, help='collection name of the Internet Archive colllection to download')
        parser.add_argument('--exporttype', type=str, required=True, help='extension to save out as (json, csv)')
        self.isTrain = False
        return parser
