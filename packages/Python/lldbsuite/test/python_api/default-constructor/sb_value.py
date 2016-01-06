"""
Fuzz tests an object after the default construction to make sure it does not crash lldb.
"""

import sys
import lldb

def fuzz_obj(obj):
    obj.GetError()
    obj.GetID()
    obj.GetName()
    obj.GetTypeName()
    obj.GetByteSize()
    obj.IsInScope()
    obj.GetFormat()
    obj.SetFormat(lldb.eFormatBoolean)
    obj.GetValue()
    obj.GetValueType()
    obj.GetValueDidChange()
    obj.GetSummary()
    obj.GetObjectDescription()
    obj.GetLocation()
    obj.SetValueFromCString("my_new_value")
    obj.GetChildAtIndex(1)
    obj.GetChildAtIndex(2, lldb.eNoDynamicValues, False)
    obj.GetIndexOfChildWithName("my_first_child")
    obj.GetChildMemberWithName("my_first_child")
    obj.GetChildMemberWithName("my_first_child", lldb.eNoDynamicValues)
    obj.GetNumChildren()
    obj.GetOpaqueType()
    obj.Dereference()
    obj.TypeIsPointerType()
    stream = lldb.SBStream()
    obj.GetDescription(stream)
    obj.GetExpressionPath(stream)
    obj.GetExpressionPath(stream, True)
    error = lldb.SBError()
    obj.Watch(True, True, False, error)
    obj.WatchPointee(True, False, True, error)
    for child_val in obj:
        s = str(child_val)
    error = lldb.SBError()
    obj.GetValueAsSigned (error, 0)
    obj.GetValueAsUnsigned (error, 0)
    obj.GetValueAsSigned(0)
    obj.GetValueAsUnsigned(0)
    obj.GetDynamicValue (lldb.eNoDynamicValues)
    obj.GetStaticValue ()
    obj.IsDynamic()
    invalid_type = lldb.SBType()
    obj.CreateChildAtOffset ("a", 12, invalid_type)
    obj.Cast (invalid_type)
    obj.CreateValueFromExpression ("pt->x", "pt->x")
    obj.CreateValueFromAddress ("x", 0x123, invalid_type)
    invalid_data = lldb.SBData()
    obj.CreateValueFromData ("x", invalid_data, invalid_type)
    obj.GetValueForExpressionPath("[0]")
    obj.AddressOf()
    obj.GetLoadAddress()
    obj.GetAddress()
    obj.GetPointeeData (0, 1)
    obj.GetData ()
    obj.GetTarget()
    obj.GetProcess()
    obj.GetThread()
    obj.GetFrame()
    obj.GetType()
