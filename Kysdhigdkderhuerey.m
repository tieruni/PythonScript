//
//  Kysdhigdkderhuerey.m
//  
//
//  Created by 朱洁珊 on 19/12/9.
//
//

#import "Kysdhigdkderhuerey.h"

@implementation Kysdhigdkderhuerey

//处理double
+(NSMutableArray *)KysdhigdkderhuereyTYs5ugt:(double)param1 yierhgiuhs:(NSString *)prefixStr uybUbuowrsd:(NSString *)sufixStr{
    NSMutableArray *mutArr = [NSMutableArray array];
    NSNumber *originNum = [NSNumber numberWithDouble:param1];
    NSString *dbstr = [originNum stringValue];
    //zf
//    [mutArr addObject:dbstr];
//    return mutArr;
    if (![dbstr containsString:@"."]) {
        [mutArr addObject:dbstr];
    }
    else{
        mutArr = [[dbstr componentsSeparatedByString:@"."] mutableCopy];
        NSString *prefstr = [[NSString stringWithFormat:@"%@--",prefixStr] stringByAppendingString:mutArr[0]];
        NSString *sufstr = [mutArr[1] stringByAppendingString:[NSString stringWithFormat:@"--%@",sufixStr]];
        mutArr[0] = prefstr;
        mutArr[1] = sufstr;
    }

    return mutArr;
}
//还原double
+(double)KysdhigdkderhuereyEJbd3sojgn:(NSMutableArray *)outArr{
    double reducedbValue = 0.0;
    //zf
//    NSString *wisdpkw = [outArr firstObject];
//    reducedbValue = [wisdpkw doubleValue];
//    return reducedbValue;
    if (outArr.count == 1) {
        NSString *wisdpkw = [outArr firstObject];
        reducedbValue = [wisdpkw doubleValue];
    }
    else{
        NSArray *arr1 = [[NSString stringWithFormat:@"%@",outArr[0]] componentsSeparatedByString:@"--"];
        NSArray *arr2 = [[NSString stringWithFormat:@"%@",outArr[1]] componentsSeparatedByString:@"--"];
        [outArr setArray:@[arr1[1],arr2[0]]];
        NSString *reducestr = [outArr componentsJoinedByString:@"."];
        reducedbValue = [reducestr doubleValue];
    }


    return reducedbValue;
}

//处理long long
+(NSData *)KysdhigdkderhuereyYsg4dfu:(long long)param1 Tusdg3erhi:(NSString *)randomStr{
    
    NSData *data = [NSData new];
    //zf
//    NSNumber *wegowher = [NSNumber numberWithLongLong:param1];
//    NSString *wguhodfher= [wegowher stringValue];
//    data = [wguhodfher dataUsingEncoding:NSUTF8StringEncoding];
//    return data;
    
    
    NSInteger randomInt = arc4random()%90+10;

    param1 += randomInt;

    NSNumber *originNum = [NSNumber numberWithLongLong:param1];

    NSString *longstr = [originNum stringValue];

    NSString *substring = [[NSString stringWithFormat:@"**%@",randomStr] stringByAppendingString:[NSString stringWithFormat:@"%ld",randomInt]];

    longstr = [longstr stringByAppendingString:substring];

    data = [longstr dataUsingEncoding:NSUTF8StringEncoding];

    return data;
}
//还原Longlong
+(long long)KysdhigdkderhuereyRdsbh9gierh:(NSData *)outLongData{
    long long reduceLongVL = 0;
    //zf
//    NSString *iwegow = [[NSString alloc] initWithData:outLongData encoding:NSUTF8StringEncoding];
//    reduceLongVL = [iwegow longLongValue];
//    return reduceLongVL;
    
    NSMutableString *outMutStr = [[[NSString alloc] initWithData:outLongData encoding:NSUTF8StringEncoding] mutableCopy];

    NSArray *outArr = [outMutStr componentsSeparatedByString:@"**"];

    NSString *originStr = [outArr firstObject];

    NSString *levStr = [outArr lastObject];

    long long chazhi = [[levStr substringFromIndex:levStr.length-2] longLongValue];

    reduceLongVL = [originStr longLongValue] - chazhi;

    return reduceLongVL;
}

//处理字符串
+(NSArray *)KysdhigdkderhuereyKshdgh2jwe:(NSString *)param1 hgvsghsdert:(NSString *)randomstr1 asghgbfiwjeg:(NSString *)randomstr2 sbgviweeroh:(UIColor *)color wayefosdgnw:(UIFont *)font{
    
    NSMutableString *mutStr = [[NSMutableString alloc] init];
//    NSData *data = [NSData new];
    NSMutableArray *mutArr = [NSMutableArray new];
    mutStr = [param1 mutableCopy];
    //zf
//    if (mutStr == nil) {
//        return nil;
//    }
//    [mutArr addObject:mutStr];
//    return mutArr;
    
    if (mutStr == nil) {
        return nil;
    }
    else if (mutStr.length == 0 || [mutStr isEqualToString:@""]){
//        data = [mutStr dataUsingEncoding:NSUTF8StringEncoding];
        [mutArr addObject:mutStr];
        return mutArr;
    }
    else{

        NSInteger len1 = randomstr1.length;
        NSInteger len2 = randomstr2.length;
        [mutStr insertString:randomstr1 atIndex:0];
        [mutStr appendString:randomstr2];
        NSAttributedString *attributeStr = [[NSAttributedString alloc] initWithString:mutStr attributes:@{NSForegroundColorAttributeName:color,NSAttachmentAttributeName:font}];
//        [mutArr addObject:attributeStr];
        [mutArr setArray:@[@(len1),attributeStr,@(len2)]];
        return mutArr;
    }
}
//还原字符串
+(NSString *)KysdhigdkderhuereyLysd7fudhk:(NSArray *)outArr{
    
    
    NSMutableString *outMutstr = [NSMutableString new];
    //zf
//    outMutstr = [[NSString stringWithFormat:@"%@",[outArr firstObject]] mutableCopy];
//    return outMutstr;
    
    if (outArr == nil) {
        return nil;
    }
    else if (outArr.count == 1 || [[NSString stringWithFormat:@"%@",[outArr firstObject]] isEqualToString:@""]){

        return [outArr firstObject];
    }
    else{
        NSAttributedString *reduceAttributeStr = [[NSAttributedString alloc] initWithAttributedString:outArr[1]];

        outMutstr = [[reduceAttributeStr string] mutableCopy];

        NSInteger reduceLen1 = [outArr[0] integerValue];
        NSString *subStr1 = [outMutstr substringToIndex:reduceLen1];
        NSRange range1 = [outMutstr rangeOfString:subStr1];
        [outMutstr deleteCharactersInRange:range1];

        NSInteger reduceLen2 = [outArr[2] integerValue];
        NSString *substr2 = [outMutstr substringFromIndex:outMutstr.length-reduceLen2];
        NSRange range2 = [outMutstr rangeOfString:substr2];
        [outMutstr deleteCharactersInRange:range2];
        return outMutstr;
    }
    
}

//处理数组
+(NSMutableDictionary *)KysdhigdkderhuereyKstd6hstd:(NSArray *)param1 title:(NSString *)substr1 color:(UIColor *)subcolor randomStr:(NSString *)randomstr{
    NSMutableDictionary *mutDic = [[NSMutableDictionary alloc] init];
    NSMutableArray *originMutArr = [[NSMutableArray alloc] initWithArray:param1];
    //zf
//    [mutDic setObject:originMutArr forKey:@"AAA"];
//    return mutDic;
    
    if (originMutArr == nil) {
        return nil;
    }
    else if (originMutArr.count == 0 /*|| [originMutArr[0] isEqualToString:@""]*/){
//        NSString *outStr = [NSString stringWithFormat:@"%@",originMutArr[0]];
        [mutDic setObject:originMutArr forKey:@"null"];

        return mutDic;
    }
    else{

        NSDictionary *attribuDic = [NSDictionary dictionary];
        int randomInt = arc4random()%66;
        if (randomInt < 36) {
            attribuDic = @{NSForegroundColorAttributeName:[UIColor colorWithRed:(arc4random()%255)/255.0 green:(arc4random()%255)/255.0 blue:(arc4random()%255)/255.0 alpha:1.0],NSAttachmentAttributeName:[UIFont boldSystemFontOfSize:16]};
        }else{
            attribuDic = @{NSForegroundColorAttributeName:subcolor};
        }
        NSMutableAttributedString *attributeStr = [[NSMutableAttributedString alloc] initWithString:substr1];
        [attributeStr setAttributes:attribuDic range:NSMakeRange(0, arc4random()%substr1.length)];

        [originMutArr addObject:attributeStr];
        [originMutArr insertObject:randomstr atIndex:0];
        originMutArr = [[[originMutArr reverseObjectEnumerator] allObjects] mutableCopy];
        [mutDic setObject:originMutArr forKey:@"content"];

        return mutDic;
    }
}
//还原数组
+(NSArray *)KysdhigdkderhuereyEtjdfb5hid:(NSMutableDictionary *)outDic{
//    return outDic[@"AAA"];
    if (outDic == nil) {
        return nil;
    }
    else if (outDic[@"null"]){
        return outDic[@"null"];
    }
    else{

        NSMutableArray *outMutArr = [outDic[@"content"] mutableCopy];
        outMutArr = [[[outMutArr reverseObjectEnumerator] allObjects] mutableCopy];

        [outMutArr removeLastObject];
        [outMutArr removeObjectAtIndex:0];

        return outMutArr;
    }
}

@end
