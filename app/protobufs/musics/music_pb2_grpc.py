# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import music_pb2 as music__pb2


class MusicsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMusic = channel.unary_unary(
                '/Musics/GetMusic',
                request_serializer=music__pb2.GetMusicRequest.SerializeToString,
                response_deserializer=music__pb2.MusicResponse.FromString,
                )
        self.GetTrendingMusics = channel.unary_unary(
                '/Musics/GetTrendingMusics',
                request_serializer=music__pb2.GetTrendingMusicsRequest.SerializeToString,
                response_deserializer=music__pb2.MusicListResponse.FromString,
                )
        self.GetTrendingMusicsByCountry = channel.unary_unary(
                '/Musics/GetTrendingMusicsByCountry',
                request_serializer=music__pb2.GetTrendingMusicsByCountryRequest.SerializeToString,
                response_deserializer=music__pb2.MusicListResponse.FromString,
                )
        self.GetTop200Musics = channel.unary_unary(
                '/Musics/GetTop200Musics',
                request_serializer=music__pb2.GetTop200MusicsRequest.SerializeToString,
                response_deserializer=music__pb2.MusicListResponse.FromString,
                )
        self.GetTop200MusicsByCountry = channel.unary_unary(
                '/Musics/GetTop200MusicsByCountry',
                request_serializer=music__pb2.GetTop200MusicsByCountryRequest.SerializeToString,
                response_deserializer=music__pb2.MusicListResponse.FromString,
                )
        self.GetViral50Musics = channel.unary_unary(
                '/Musics/GetViral50Musics',
                request_serializer=music__pb2.GetViral50MusicsRequest.SerializeToString,
                response_deserializer=music__pb2.MusicListResponse.FromString,
                )
        self.GetViral50MusicsByCountry = channel.unary_unary(
                '/Musics/GetViral50MusicsByCountry',
                request_serializer=music__pb2.GetViral50MusicsByCountryRequest.SerializeToString,
                response_deserializer=music__pb2.MusicListResponse.FromString,
                )
        self.GetMostStreamedMusics = channel.unary_unary(
                '/Musics/GetMostStreamedMusics',
                request_serializer=music__pb2.GetMostStreamedMusicsRequest.SerializeToString,
                response_deserializer=music__pb2.MusicListResponse.FromString,
                )


class MusicsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetMusic(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTrendingMusics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTrendingMusicsByCountry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTop200Musics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTop200MusicsByCountry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetViral50Musics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetViral50MusicsByCountry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMostStreamedMusics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MusicsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMusic': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMusic,
                    request_deserializer=music__pb2.GetMusicRequest.FromString,
                    response_serializer=music__pb2.MusicResponse.SerializeToString,
            ),
            'GetTrendingMusics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTrendingMusics,
                    request_deserializer=music__pb2.GetTrendingMusicsRequest.FromString,
                    response_serializer=music__pb2.MusicListResponse.SerializeToString,
            ),
            'GetTrendingMusicsByCountry': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTrendingMusicsByCountry,
                    request_deserializer=music__pb2.GetTrendingMusicsByCountryRequest.FromString,
                    response_serializer=music__pb2.MusicListResponse.SerializeToString,
            ),
            'GetTop200Musics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTop200Musics,
                    request_deserializer=music__pb2.GetTop200MusicsRequest.FromString,
                    response_serializer=music__pb2.MusicListResponse.SerializeToString,
            ),
            'GetTop200MusicsByCountry': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTop200MusicsByCountry,
                    request_deserializer=music__pb2.GetTop200MusicsByCountryRequest.FromString,
                    response_serializer=music__pb2.MusicListResponse.SerializeToString,
            ),
            'GetViral50Musics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetViral50Musics,
                    request_deserializer=music__pb2.GetViral50MusicsRequest.FromString,
                    response_serializer=music__pb2.MusicListResponse.SerializeToString,
            ),
            'GetViral50MusicsByCountry': grpc.unary_unary_rpc_method_handler(
                    servicer.GetViral50MusicsByCountry,
                    request_deserializer=music__pb2.GetViral50MusicsByCountryRequest.FromString,
                    response_serializer=music__pb2.MusicListResponse.SerializeToString,
            ),
            'GetMostStreamedMusics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMostStreamedMusics,
                    request_deserializer=music__pb2.GetMostStreamedMusicsRequest.FromString,
                    response_serializer=music__pb2.MusicListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Musics', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Musics(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetMusic(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Musics/GetMusic',
            music__pb2.GetMusicRequest.SerializeToString,
            music__pb2.MusicResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTrendingMusics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Musics/GetTrendingMusics',
            music__pb2.GetTrendingMusicsRequest.SerializeToString,
            music__pb2.MusicListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTrendingMusicsByCountry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Musics/GetTrendingMusicsByCountry',
            music__pb2.GetTrendingMusicsByCountryRequest.SerializeToString,
            music__pb2.MusicListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTop200Musics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Musics/GetTop200Musics',
            music__pb2.GetTop200MusicsRequest.SerializeToString,
            music__pb2.MusicListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTop200MusicsByCountry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Musics/GetTop200MusicsByCountry',
            music__pb2.GetTop200MusicsByCountryRequest.SerializeToString,
            music__pb2.MusicListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetViral50Musics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Musics/GetViral50Musics',
            music__pb2.GetViral50MusicsRequest.SerializeToString,
            music__pb2.MusicListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetViral50MusicsByCountry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Musics/GetViral50MusicsByCountry',
            music__pb2.GetViral50MusicsByCountryRequest.SerializeToString,
            music__pb2.MusicListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMostStreamedMusics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Musics/GetMostStreamedMusics',
            music__pb2.GetMostStreamedMusicsRequest.SerializeToString,
            music__pb2.MusicListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)